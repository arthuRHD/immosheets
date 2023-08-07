# Development guidelines

## Commit message style

I like adding gitmoji inside the commit message. I think this is a great way to visualize changes and value everyone's time.

https://gitmoji.dev/

## How to release

First, you need to be on the master branch and make sure it's up to date

```sh
git checkout master
git pull
```

Then, procede to change the version inside the `setup.py` file

```py
...
setup(
    name="immosheets",
    version="1.0.0", # <- Change here
...
```

Commit the change this way

```sh
git add setup.py
git commit -m ":bookmark: : 1.0.0 -> 1.0.1"
git push
```

Create a tag and push it to trigger Github Actions pipeline. This will deploy the new package on PyPI.

```sh
git tag 1.0.0
git push origin 1.0.0
```
