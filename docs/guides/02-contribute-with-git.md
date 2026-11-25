# 2. Contribute directly with Git and Markdown

You can contribute in the GitHub web interface without installing anything, or locally with Git.

## Option A: in the browser (no installation)

1. Open the file you want to change under `framework/`, or the folder where a new node should go.
2. Click the pencil icon (**Edit this file**), or **Add file → Create new file**. For a new node, paste the content of [templates/node-template.md](../../templates/node-template.md).
3. Make your changes. Use **Preview** to check the formatting.
4. Click **Commit changes…**, choose **Create a new branch for this commit and start a pull request**, give the branch a short name (e.g. `imp-model-registries`) and click **Propose changes**.
5. Fill in the pull request template and click **Create pull request**.

You can keep committing to the same branch. The pull request updates automatically.

## Option B: locally with Git

```bash
git clone https://github.com/AIML4OS/WP5.git
cd WP5
pip install -r requirements.txt          # once
git switch -c imp-model-registries       # a new branch for your change
# ... edit files ...
python tools/wp5.py validate             # check before you push
git add framework/
git commit -m "Draft extended description of model registries"
git push -u origin imp-model-registries
```

Then open the pull request on GitHub.

## Good practice

- **One topic per pull request.** Several small PRs are easier to review than one large one.
- **Keep nodes small** (about one to two pages). If a node grows, split it and link the parts.
- **Cite as you write.** Add the source to `references/references.yaml` if it is not there yet, and give a `locator` (section, page, table).
- **Do not rename ids** of merged nodes; other nodes link to them. You can change the title freely.
- **Use comments for notes**: `<!-- TODO: ... -->` or `<!-- Review note: ... -->` are kept in the file but left out of all outputs.
- **Write in English.**

## Working on someone else's node

Open a pull request as usual and add the owners as reviewers. For small language fixes, that is enough. For changes in substance, discuss in the PR or the task group first.
