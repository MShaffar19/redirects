"""
    test_redirects
    ~~~~~~~~~~~

    Test the sphinxcontrib.redirects module.

    :copyright: Copyright 2017 by Stephen Finucane <stephen@that.guru>
    :license: BSD, see LICENSE for details.
"""

import pytest


@pytest.mark.sphinx('html', testroot='flat_dir',
    confoverrides={'extensions': ['sphinxcontrib.redirects']})
def test_flat_dir(app, status, warning):
    """Ensure a simple flat tree structure works."""
    app.builder.build_all()

    content = (app.outdir / 'testing.html').text()
    assert (u'<head><meta http-equiv="refresh" content="0; '
            'url=test.html"/></head>' in content)


@pytest.mark.sphinx('html', testroot='nested_dir',
    confoverrides={'extensions': ['sphinxcontrib.redirects']})
def test_nested_dir(app, status, warning):
    """Ensure a more complicated nested tree structure works.

    We test both nested real docs and nested redirect docs.
    """
    app.builder.build_all()

    content = (app.outdir / 'work/index.html').text()
    assert (u'<head><meta http-equiv="refresh" content="0; '
            'url=../stuff/index.html"/></head>' in content)

    content = (app.outdir / 'well/well/index.html').text()
    assert (u'<head><meta http-equiv="refresh" content="0; '
            'url=../../test.html"/></head>' in content)
