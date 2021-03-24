from typing import Any, Mapping, MutableMapping

from markdown_it import MarkdownIt
from mdformat.renderer import RenderTreeNode
from mdformat.renderer.typing import RendererFunc


def update_mdit(mdit: MarkdownIt) -> None:
    """Update the parser, e.g. by adding a plugin: `mdit.use(myplugin)`"""
    pass


def _render_table(
    node: RenderTreeNode,
    renderer_funcs: Mapping[str, RendererFunc],
    options: Mapping[str, Any],
    env: MutableMapping,
) -> str:
    """Render a `RenderTreeNode` of type "table".

    Change "table" to the name of the syntax you want to render.
    """
    return ""


# A mapping from syntax tree node to a function that renders it.
# This can be used to overwrite renderer functions of existing syntax
# or add support for new syntax.
RENDERER_FUNCS: Mapping[str, RendererFunc] = {"table": _render_table}
