---

# How to Build a Python Package

## Basics

- Learn about the differences between the [src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).
- Watch this video on [Packaging Your Python Code With pyproject.toml](https://www.youtube.com/watch?v=v6tALyc4C10) to understand the basics of Python packaging.

## Steps

1. **Create a `pyproject.toml` File**
    - Follow the guide on [Configuring setuptools using pyproject.toml files](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html).

2. **[Optional] Install the Package in Editable Mode**
    ```sh
    pip install -e .
    ```

3. **Build the Package**
    ```sh
    python3 -m build
    ```

4. **Upload to GitLab**

    1. Append the following to `~/.pypirc` by running `nano ~/.pypirc`:
        ```ini
        [distutils]
        index-servers =
            gitlab

        [gitlab]
        repository = https://{{gitlab-base-url}}/api/v4/projects/{{your-project-id}}/packages/pypi
        username = {{your-token-name}}
        password = {{your-token-value}}
        ```

        - `{{gitlab-base-url}}`: For GitLab cloud users, the value is simply `gitlab.com`. For other GitLab users, the value might be something like `gitlab.yourcompany.com`.
        - `{{your-project-id}}`: Your numeric project ID, e.g., 29074488.
        - `{{your-token-name}}`: The name of your GitLab personal access token, e.g., `pip-access-token`.
        - `{{your-token-value}}`: Your token value, e.g., `9rdzBgYLB7_xMGFFoUFn`.

    2. Run the command to upload your package:
        ```sh
        python3 -m twine upload --repository gitlab dist/*
        ```

5. **Install the Package from GitLab**
    ```sh
    pip install my-package -U --extra-index-url https://__token__:<GITLAB_TOKEN>@{{gitlab-base-url}}/api/v4/projects/{{your-project-id}}/packages/pypi/simple
    ```

## Resources
- [Src Layout vs Flat Layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- [How to Upload Private Python Packages to GitLab](https://medium.com/@matt_tich/how-to-upload-private-python-packages-to-gitlab-2999e9604603)
- [Build Your First Python Package with pyproject.toml](https://medium.com/@codebyteexplorer/build-your-first-python-package-with-pyproject-toml-19e2119edbca)
- [Pip Install Package from GitLab Package Registry and Dependencies from PyPI Mirror Index](https://discuss.python.org/t/pip-install-package-from-gitlab-package-registry-and-dependencies-from-pypi-mirror-index/39412)
- [Configuring Setuptools using pyproject.toml Files](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
- [Packaging Your Python Code With pyproject.toml (YouTube Video)](https://www.youtube.com/watch?v=v6tALyc4C10)
- [GitLab PyPI Repository Documentation](https://docs.gitlab.com/ee/user/packages/pypi_repository/)

---