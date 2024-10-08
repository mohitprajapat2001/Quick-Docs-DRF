# Quick Docs DRF

## Overview

Quick Docs DRF is a tool for generating `documentation` for `Django REST Framework` projects with customizable `UI templates`. It automates the `documentation` process with just simple `configuration` in project settings, and it automatically generates `documentation` based on views & serializers.

## Features

- Generate documentation with a simple command.
- Multiple UI templates (Tailwind CSS, Bootstrap).
- Global project settings for easy configuration.

## Default Settings

Here is Deafult Setting Configuration:

```python
DEFAULT = {
    "PROJECT_NAME": None,
    "PROJECT_DESCRIPTION": None,
    "VERSION": 1.0,
    "AUTHOR": None,
    "AUTHOR_EMAIL": None,
    "LICENSE": "MIT",
    "API_URL": "/api/",
    "API_VERSION": "v1",
    "API_PREFIX": "api",
    "BASE_URL":  None,
    "BASE_ROUTER_NAME": "router",
    "NESTED_ROUTER_NAME": None,
    "CONTRIBUTION": True,
    "CONTACT_SECTION": True,
    "SOCIAL_SECTION": True,
    "CONTACT": {
        "name":  None,
        "email":  None,
        "url":  None,
    },
    "SOCIAL": {
        "github": None,
        "twitter": None,
        "linkedin": None,
        "facebook": None,
        "instagram": None,
        "youtube": None,
        "medium": None,
    },
}
```

## Installation

To install Quick Docs DRF, run the following command:

```bash
pip install quick_docs_drf
```

## Usage

Usage detail overview available soon.

## Contribution

We welcome contributions! If you'd like to contribute, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or feedback, feel free to reach out at:  

- Email: [mohit.prajapat@trootech.com]
