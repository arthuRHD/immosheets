import os
import logging

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError

from ..real_estate import RealEstate
from ..settings import settings
from ..reporting_service import ReportingService


class GoogleSpreadsheetsService(ReportingService):
    """Override the default service to communicate with Google Sheets API."""

    def __init__(self, credentials_file_path: str) -> None:
        self.scope = [settings.google_api_scope]
        self.sheet_id = None
        self.logger = logging.getLogger(__name__)
        self.credentials_file_path = credentials_file_path
        super().__init__()
        self.range: str = settings.google_sheets_range_name
        self.service: Resource = build('sheets', 'v4', credentials=self.creds)

    def auth(self):
        token_path: str = os.path.join(os.getcwd(), 'token.json')
        if os.path.exists(token_path):
            self.creds = Credentials.from_authorized_user_file(
                token_path, self.scope)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file_path, self.scope)
                self.creds = flow.run_local_server(port=0)
            with open(token_path, 'w', encoding="utf-8") as token:
                token.write(self.creds.to_json())

    def use(self, new_google_sheet_id: str):
        """Override the default spreadsheet id with the given one.

        :param new_google_sheet_id: The new spreadsheet id
        :type new_google_sheet_id: str
        :return: The instance of the service so you can chain methods.
        :rtype: GoogleSpreadsheetsService
        """
        self.sheet_id = new_google_sheet_id
        self.logger.info("using %s.", self.sheet_id)
        return self

    def clear(self):
        self.service.spreadsheets().values().clear(
            spreadsheetId=self.sheet_id, range=self.range).execute()
        self.logger.info("%s cells cleared.", self.sheet_id)
        return self

    def add_headers(self):
        try:
            sheet = self.service.spreadsheets()
            sheet.values().append(
                spreadsheetId=self.sheet_id,
                range=self.range,
                valueInputOption="USER_ENTERED",
                body={'values': [['price', 'bedrooms', 'rooms', 'city',
                                  'm²', 'link', 'contact', 'email', 'tel', 'provider']]}
            ).execute()

            self.logger.info("headers added on %s.", self.sheet_id)
        except HttpError as err:
            self.logger.error(err)
        return self

    def insert(self, real_estates: list[RealEstate]):
        try:
            sheet = self.service.spreadsheets()
            to_insert = []
            for real_estate in real_estates:
                to_insert.append(real_estate.to_cell())
            result = sheet.values().append(
                spreadsheetId=self.sheet_id,
                range=self.range,
                valueInputOption="USER_ENTERED",
                body={'values': to_insert}
            ).execute()

            self.logger.info(
                "%s cells appended to %s", result.get('updates').get('updatedCells'), self.sheet_id)

        except HttpError as err:
            self.logger.error(err)
