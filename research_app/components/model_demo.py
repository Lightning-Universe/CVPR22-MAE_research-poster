import logging

import gradio as gr
from lightning.app.components.serve import ServeGradio
from PIL import Image
from rich.logging import RichHandler

from research_app.mae_demo import Demo

FORMAT = "%(message)s"
logging.basicConfig(level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])

logger = logging.getLogger(__name__)


class ModelDemo(ServeGradio):
    """Serve model with Gradio UI.

    You need to define i. `build_model` and ii. `predict` method and Lightning `ServeGradio` component will
    automatically launch the Gradio interface.
    """

    inputs = gr.inputs.Image(type="pil")
    outputs = [
        gr.outputs.Image(label="original image"),
        gr.outputs.Image(label="masked"),
        gr.outputs.Image(label="reconstructed"),
        gr.outputs.Image(label="reconstructed + visible"),
    ]

    enable_queue = True

    def __init__(self):
        super().__init__(parallel=True)

    def build_model(self) -> Demo:
        logger.info("loading model...")
        model = Demo()
        logger.info("built model!")
        return model

    def predict(self, image: Image.Image) -> Image.Image:
        result = self.model.predict(image)
        return result["original"], result["masked"], result["reconstructed"], result["visible"]
