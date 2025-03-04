import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session
def html(session):
    """Builds the html for the site locally for static rendering."""
    session.install("-r", "requirements.txt")
    session.install("quarto-cli")
    session.install("-e", "./pyosmetrics_pkg")
    cmd = ["quarto", "render"]
    session.run(*cmd)


@nox.session
def serve(session):
    """Builds the quarto site locally using quarto preview. Opens a local host
    which allows for a live preview that updates as you work."""
    session.install("-r", "requirements.txt")
    session.install("quarto-cli")
    session.install("-e", "./pyosmetrics_pkg")
    cmd = ["quarto", "preview"]
    session.run(*cmd)
