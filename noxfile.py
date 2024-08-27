import nox

nox.options.reuse_existing_virtualenvs = True

build_serve = ["start", "--execute"]

build_execute = ["build", "--html", "--execute"]


@nox.session
def html(session):
    session.install("-r", "requirements.txt")
    cmd = ["myst"]
    cmd.extend(build_execute + session.posargs)
    session.run(*cmd)


@nox.session
def serve(session):
    session.install("-r", "requirements.txt")
    session.install("-e", "./pyosmetrics_pkg")
    cmd = ["myst"]
    cmd.extend(build_serve + session.posargs)
    session.run(*cmd)
