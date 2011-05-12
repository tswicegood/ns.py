ns.py
=====
Declaring namespaces in one Python file

Ever feel that having a requirement on ``pkg_resources`` just so you can do
sane namespaces in Python is a little much?  If so, this package is for you.
It aims to be a simple, one-file replacement for that single function and all
of the craziness it adds.


.. warning:: This isn't production ready yet.  It's got tests, and those tests
             have been run on exactly two platforms.  Not what you'd call
             battle-tested.  *But* if you're interested in making a viable
             alternative to ``pkg_resources`` for Python, please fork this
             project and help.

Usage
-----
It's simple.  You import ``declare``, and call it.

::

    from ns import declare
    declare(__name__)


Acknowledgements
----------------
``pkg_resources`` provided the jumping off point for this code.  Without it,
I'd probably still be scratching my head over recursively walking the module
path.

`Peter Wang`_ convinced me over beer that we should try to do this.

Contributing
------------

* Create something awesome -- make the code better, add some functionality,
  whatever (this is the hardest part).
* `Fork it`_
* Create a topic branch to house your changes
* Get all of your commits in the new topic branch
* Submit a `pull request`_

.. _pull request: http://help.github.com/pull-requests/
.. _Fork it: http://help.github.com/forking/
.. _Peter Wang: http://blog.streamitive.com/
