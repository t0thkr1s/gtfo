# PyPI Publishing Setup Guide

This guide will help you set up automatic publishing to PyPI using GitHub Actions.

## Prerequisites

1. PyPI account: https://pypi.org/account/register/
2. Test PyPI account (optional): https://test.pypi.org/account/register/

## Step 1: Generate API Tokens

### For PyPI (Production)

1. Log in to https://pypi.org
2. Go to Account Settings → API tokens
3. Click "Add API token"
4. Token name: `github-actions-gtfobins`
5. Scope: Select "Entire account" (for first upload) or specific project after first upload
6. Copy the token (starts with `pypi-`)

### For Test PyPI (Optional)

1. Log in to https://test.pypi.org
2. Follow the same steps as above
3. Token name: `github-actions-gtfobins-test`

## Step 2: Add Secrets to GitHub Repository

1. Go to your repository on GitHub
2. Navigate to Settings → Secrets and variables → Actions
3. Click "New repository secret"

Add these secrets:
- Name: `PYPI_API_TOKEN`
  Value: Your PyPI token (from Step 1)
  
- Name: `TEST_PYPI_API_TOKEN` (optional)
  Value: Your Test PyPI token

## Step 3: Test the Setup

### Test with Test PyPI (Recommended)

1. Make a commit to main/master branch
2. Check Actions tab for build status
3. If successful, package will be available at:
   ```
   https://test.pypi.org/project/gtfobins/
   ```

### Install from Test PyPI

```bash
pip install -i https://test.pypi.org/simple/ gtfobins
```

## Step 4: Production Release

To publish to production PyPI:

1. Create a new tag:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

2. The GitHub Action will automatically:
   - Run tests
   - Build the package
   - Publish to PyPI

3. Install from PyPI:
   ```bash
   pip install gtfobins
   ```

## Versioning

Remember to update the version in these files before creating a new release:
- `gtfo/__init__.py`
- `setup.py`
- `setup.cfg`
- `pyproject.toml`

## Manual Publishing (Alternative)

If you prefer manual publishing:

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Check the package
twine check dist/*

# Upload to Test PyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

## Troubleshooting

### Common Issues

1. **Token scope error**: For first upload, use "Entire account" scope
2. **Package name conflict**: The name might be taken, consider `gtfobins-cli`
3. **Version conflict**: Ensure version number is incremented

### Verification

After publishing, verify your package:

```bash
# Create a new virtual environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install your package
pip install gtfobins

# Test it
gtfo --version
gtfo bash
```

## Security Notes

- Never commit tokens to the repository
- Rotate tokens periodically
- Use Test PyPI for testing before production releases
- Consider using trusted publishing with OIDC (newer GitHub feature)
