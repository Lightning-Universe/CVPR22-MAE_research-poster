# ⚡️ Masked Autoencoders CVPR-22 Research Poster 🔬

This app is a research poster demo of Masked Autoencoders model by Facebook Research. It showcases a notebook and a model demo where you can upload photos to get a visualization of image reconstruction.

## Getting started

To create a Research Poster, you can install this app via the [Lightning CLI](https://lightning.ai/lightning-docs/) or [use the template](https://docs.github.com/en/articles/creating-a-repository-from-a-template) from GitHub and manually install the app as mentioned below.

### Installation

#### With Lightning CLI

`lightning install app lightning/research_poster`

#### Use GitHub template

Click on the "Use this template" button at the top, name your app repo, and GitHub will create a fork of this app to your account.

> ![use-template.png](./assets/use-template.png)

You can clone the forked app repo and follow the steps below to install the app.

```
git clone https://github.com/YOUR-USERNAME/lightning-template-research-app.git
cd lightning-template-research-app
pip install -r requirements.txt
pip install -e .
```

Once you have installed the app, you can go to the `lightning-template-research-app` folder. Running `lightning run app app.py --cloud` from your terminal will launch the template app in your default browser with tabs containing research paper, blog, training logs and model demo.

You should see something like this in your browser:

> ![image](./assets/demo.png)

You can modify the content of this app and customize it to your research. At the root of this template, you will find [app.py](./app.py) which contains the `ResearchApp` class. This class provides arguments, such as a link to a paper, a blog and whether to launch a Gradio demo. You can read more about what each argument does in the docstrings.

### Highlights

- Provide a link for your paper, blog, or training logger, such as WandB, as an argument, and `ResearchApp` will create a tab for each.
- Make a poster for your research by editing the markdown file in the [resources](./resources/poster.md) folder.
- Add an interactive model demo with Gradio, update the Gradio component present in the [research_app](./research_app/components/model_demo.py) directory.
- View a Jupyter Notebook or launch a fully-fledged notebook instance (Sharing a Jupyter Notebook instance can expose the cloud instance to security vulnerability.)
- Reorder the tab layout using the `tab_order` argument.

### Example

```python
# update app.py at the root of the repo
import lightning as L

paper = "https://arxiv.org/pdf/2103.00020.pdf"
blog = "https://openai.com/blog/clip/"
github_url = "https://github.com/mlfoundations/open_clip"
wandb_url = "https://wandb.ai/aniketmaurya/herbarium-2022/runs/2dvwrme5"
tabs = ["Poster", "Blog", "Paper", "Notebook", "Training Logs", "Model Demo"]

app = L.LightningApp(
    ResearchApp(
        poster_dir="resources",
        paper=paper,
        blog=blog,
        training_log_url=wandb_url,
        github=github_url,
        notebook_path="resources/Interacting_with_CLIP.ipynb",
        launch_jupyter_lab=False,
        launch_gradio=True,
        tab_order=tabs,
    )
)
```

## FAQs

1. How to pull from the latest template code? [Answer](https://stackoverflow.com/questions/56577184/github-pull-changes-from-a-template-repository)
