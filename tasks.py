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
    c.run("sphinx-autobuild source/ build/")