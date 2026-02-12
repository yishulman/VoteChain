import shutil
from invoke import task


@task
def build_doc(c):
    """
    Build and serve Sphinx documentation with live reloading.

    Runs the command "sphinx-autobuild source/ build/" using the provided task
    context so documentation is rebuilt and served automatically on changes.

    Parameters
    ----------
    c : invoke.Context
        Task runner context used to execute shell commands.

    Returns
    -------
    None
    """
    if shutil.which("sphinx-autobuild") is None:
        raise SystemExit(
            "Error: 'sphinx-autobuild' not found. "
            "Install dependencies with: pip install -r requirements.txt"
        )

    c.run("sphinx-autobuild source/ build/")
