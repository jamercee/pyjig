

<!doctype html>


<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    
    <title>pyjig - Quickly create python projects from templates &mdash; Pyjig 1.0.1 documentation</title>
    
    <link rel="stylesheet" href="_static/bizstyle.css" type="text/css" />
    <link rel="stylesheet" href="_static/pygments.css" type="text/css" />
    
    <script type="text/javascript">
      var DOCUMENTATION_OPTIONS = {
        URL_ROOT:    './',
        VERSION:     '1.0.1',
        COLLAPSE_INDEX: false,
        FILE_SUFFIX: '.html',
        HAS_SOURCE:  true
      };
    </script>
    <script type="text/javascript" src="_static/jquery.js"></script>
    <script type="text/javascript" src="_static/underscore.js"></script>
    <script type="text/javascript" src="_static/doctools.js"></script>
    <script type="text/javascript" src="_static/bizstyle.js"></script>
    <link rel="top" title="Pyjig 1.0.1 documentation" href="#" />
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <!--[if lt IE 9]>
    <script type="text/javascript" src="_static/css3-mediaqueries.js"></script>
    <![endif]-->
  </head>
  <body role="document">
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="genindex.html" title="General Index"
             accesskey="I">index</a></li>
        <li class="right" >
          <a href="py-modindex.html" title="Python Module Index"
             >modules</a> |</li>
        <li class="nav-item nav-item-0"><a href="#">Pyjig 1.0.1 documentation</a> &raquo;</li> 
      </ul>
    </div>
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
        <div class="sphinxsidebarwrapper">
  <h3><a href="#">Table Of Contents</a></h3>
  <ul>
<li><a class="reference internal" href="#"><code class="docutils literal"><span class="pre">pyjig</span></code> - Quickly create python projects from templates</a><ul>
<li><a class="reference internal" href="#project-motivation">Project Motivation</a></li>
<li><a class="reference internal" href="#project-layout">Project Layout</a></li>
<li><a class="reference internal" href="#makefile-generation">Makefile generation</a></li>
<li><a class="reference internal" href="#static-analysis">Static Analysis</a></li>
<li><a class="reference internal" href="#code-documentation">Code Documentation</a></li>
<li><a class="reference internal" href="#verision-control">Verision Control</a></li>
<li><a class="reference internal" href="#pyjig-name">Pyjig Name</a><ul>
<li><a class="reference internal" href="#command-line-options">Command line options</a><ul>
<li><a class="reference internal" href="#positional-arguments">Positional arguments</a></li>
<li><a class="reference internal" href="#optional-argument">Optional argument:</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><a class="reference internal" href="#indices-and-tables">Indices and tables</a></li>
</ul>

  <div role="note" aria-label="source link">
    <h3>This Page</h3>
    <ul class="this-page-menu">
      <li><a href="_sources/index.txt"
            rel="nofollow">Show Source</a></li>
    </ul>
   </div>
<div id="searchbox" style="display: none" role="search">
  <h3>Quick search</h3>
    <form class="search" action="search.html" method="get">
      <input type="text" name="q" />
      <input type="submit" value="Go" />
      <input type="hidden" name="check_keywords" value="yes" />
      <input type="hidden" name="area" value="default" />
    </form>
    <p class="searchtip" style="font-size: 90%">
    Enter search terms or a module, class or function name.
    </p>
</div>
<script type="text/javascript">$('#searchbox').show(0);</script>
        </div>
      </div>

    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body" role="main">
            
  <span class="target" id="module-pyjig.pyjig"></span><div class="section" id="module-pyjig">
<span id="pyjig-quickly-create-python-projects-from-templates"></span><h1><a class="reference internal" href="#module-pyjig" title="pyjig: Quickly create python projects from templates"><code class="xref py py-mod docutils literal"><span class="pre">pyjig</span></code></a> - Quickly create python projects from templates<a class="headerlink" href="#module-pyjig" title="Permalink to this headline">¶</a></h1>
<p>Pyjig quickly creates new python projects using pre-created templates. Projects
can be simple scripts, distutils packages or full blown applications.  Pyjig
can even add python source modules to existing projects.</p>
<p>Pyjig is a wrapper around <a class="reference external" href="http://cookiecutter.rtfd.org">Cookiecutter</a>,
which is a command-line utility that creates projects from <code class="docutils literal"><span class="pre">cookiecutters</span></code>
(project templates). Templates are downloaded from public repos (such as
github.com and bitbucket.org). Templates are written in <a class="reference external" href="http://jina.pocoo.org">Jinja</a>.</p>
<p>Pyjig uses three public repos:</p>
<table border="1" class="docutils">
<colgroup>
<col width="60%" />
<col width="40%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Repo</th>
<th class="head">Description</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><a class="reference external" href="https://github.org/jamercee/cookiecutter-pyapp">https://github.org/jamercee/cookiecutter-pyapp</a></td>
<td>Python application type projects</td>
</tr>
<tr class="row-odd"><td><a class="reference external" href="https://github.org/jamercee/cookiecutter-pypkg">https://github.org/jamercee/cookiecutter-pypkg</a></td>
<td>Python package type projects</td>
</tr>
<tr class="row-even"><td><a class="reference external" href="https://github.org/jamercee/cookiecutter-pysource">https://github.org/jamercee/cookiecutter-pysource</a></td>
<td>Crete python source file(s)</td>
</tr>
</tbody>
</table>
<div class="section" id="project-motivation">
<h2>Project Motivation<a class="headerlink" href="#project-motivation" title="Permalink to this headline">¶</a></h2>
<p>Using python requires developers to employ a full ecosystem of tools. At
Carroll-Net, all projects require the following tools; <a class="reference external" href="http://www.pylint.org">pylint</a> and <a class="reference external" href="https://pypi.python.org/pypi/flake8">flake8</a>
for static code analysis, <a class="reference external" href="http://sphinx-doc.org">sphinx</a> for project
documents and <a class="reference external" href="http://git-scm.com">git</a> for revision control.  And this
requires setting up directories, config files, a unittest infrastructure and a
comprehensive Makefile for automating the daily build, test, install tasks.</p>
<p>With all these steps, it&#8217;s easy to miss one, or to make a typo when copying
from another project which then caused developers to spend time debugging.
What was needed was a way to ensure uniform deployment and configuration of our
python architecture and toolchain.</p>
</div>
<div class="section" id="project-layout">
<h2>Project Layout<a class="headerlink" href="#project-layout" title="Permalink to this headline">¶</a></h2>
<p>Each new project will create the following directories and files:</p>
<div class="highlight-python"><div class="highlight"><pre>myproj               Project root
+
|
|   .gitignore
|   id.txt
|   Makefile
|   pylint.rc
|   setup.cfg
|   setup.py
|
+---.git             Git repository
|       ...
|
+---docs             Sphinx documentation
|       conf.py
|       index.rst
|       make.bat
|       Makefile
|
+---src              Project source code
|   \---myproj
|           __init__.py
|
\---tests            Unittest infrastructure
        __init__.py
</pre></div>
</div>
</div>
<div class="section" id="makefile-generation">
<h2>Makefile generation<a class="headerlink" href="#makefile-generation" title="Permalink to this headline">¶</a></h2>
<p>Each project will have a customized <code class="docutils literal"><span class="pre">Makefile</span></code> installed in the project&#8217;s
root directory. It&#8217;s syntax is written to support <a class="reference external" href="http://gnu.org/software/make">GNU Make</a>. It comes with the following pre-built recipes</p>
<table border="1" class="docutils">
<colgroup>
<col width="15%" />
<col width="85%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Recipe</th>
<th class="head">Description</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>comp</td>
<td>Perform static analysis (default target)</td>
</tr>
<tr class="row-odd"><td>tests</td>
<td>Run unittests</td>
</tr>
<tr class="row-even"><td>docs</td>
<td>Generate html documentation</td>
</tr>
<tr class="row-odd"><td>dist</td>
<td>Build python package</td>
</tr>
<tr class="row-even"><td>install</td>
<td>Perform static analysis, run unittests and install to site-packages</td>
</tr>
<tr class="row-odd"><td>viewdocs</td>
<td>Rebuild html docs &amp; launch browser</td>
</tr>
<tr class="row-even"><td>clean</td>
<td>Meta-recipe to invoke <code class="docutils literal"><span class="pre">clean-build</span></code>, <code class="docutils literal"><span class="pre">clean-pyc</span></code>, <code class="docutils literal"><span class="pre">clean-docs</span></code></td>
</tr>
<tr class="row-odd"><td>clean-build</td>
<td>Remove all built outputs</td>
</tr>
<tr class="row-even"><td>clean-pyc</td>
<td>Remove python built elements (*.pyc, *.pyo, etc...)</td>
</tr>
<tr class="row-odd"><td>debug</td>
<td>Generate Makefile diagnostic output</td>
</tr>
<tr class="row-even"><td>help</td>
<td>Display Makefile help</td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="static-analysis">
<h2>Static Analysis<a class="headerlink" href="#static-analysis" title="Permalink to this headline">¶</a></h2>
<p>Python&#8217;s flexible syntax means that coding errors are difficult to detect until
runtime. Static analysis tries to solve this by scanning code for coding
errors, bugs and bad style. It is an invaluable technique that has saved us
untold hours in debugging.</p>
<p>We first started using <a class="reference external" href="http://www.pylint.org">pylint</a>. Then later on we
added a second static analysis tool <a class="reference external" href="https://pypi.python.org/pypi/flake8">flake8</a>. Each tool has it&#8217;s strengths and we&#8217;ve
found the combination of both has provided material reduction in time spent
debugging.</p>
<p>Each of these two tools requires some tweaking before they will generate useful
advice.  Pyjig will handle configuring sane defaults for new projects to get
them up to speed quickly.</p>
<p>To perform static analysis of code, from within the project&#8217;s root folder run
<code class="docutils literal"><span class="pre">make</span> <span class="pre">comp</span></code>.</p>
<div class="admonition note">
<p class="first admonition-title">Note</p>
<p class="last">The <code class="docutils literal"><span class="pre">Makefile</span></code> recipe detects changes in <code class="docutils literal"><span class="pre">*.py</span></code> with reference to <code class="docutils literal"><span class="pre">*.pyc</span></code>.
If the <code class="docutils literal"><span class="pre">*.pyc</span></code> is missing or older than it&#8217;s <code class="docutils literal"><span class="pre">*.py</span></code>, a static analysis
pass will be done, and if the pass does not generate errors or warnings, the
<code class="docutils literal"><span class="pre">*.pyc</span></code> will be re-built.</p>
</div>
</div>
<div class="section" id="code-documentation">
<h2>Code Documentation<a class="headerlink" href="#code-documentation" title="Permalink to this headline">¶</a></h2>
<p>Carroll-Net has adopted <a class="reference external" href="http://sphinx-doc.org">Sphinx</a> as our documentation
generator for python projects. Sphinx converts <a class="reference external" href="https://en.wikipedia.org/wiki/ReStructuredText">reStructuredText</a> into HTML websites. Sphinx
can extract documentation from source modules and automatically generate
browesable websites.</p>
<p>There are two Makefile recipes related to documentation; <code class="docutils literal"><span class="pre">make</span> <span class="pre">docs</span></code> which
will rebuild documentation and <code class="docutils literal"><span class="pre">make</span> <span class="pre">viewdocs</span></code> which will rebuild docs and
launch a webbrowser to read the rebuilt docs.</p>
<p>Two good references for authoring reST documents are</p>
<blockquote>
<div><ul class="simple">
<li><a class="reference external" href="https://docs.python.org/devguide/documenting.html">https://docs.python.org/devguide/documenting.html</a></li>
<li><a class="reference external" href="https://pythonhosted.org/an_example_pypi_project/sphinx.html">https://pythonhosted.org/an_example_pypi_project/sphinx.html</a></li>
</ul>
</div></blockquote>
</div>
<div class="section" id="verision-control">
<h2>Verision Control<a class="headerlink" href="#verision-control" title="Permalink to this headline">¶</a></h2>
<p>Carroll-Net has adopted <a class="reference external" href="http://git-scm.org">Git</a> as our version control
system for software. Git is a fast, reliable distributed revision control
system. Originally developed for Linux kernel development it is now the most
widely used source code management tool.</p>
<p>Pyjig will initialize a git repository for each new project it creates using
your local sytem defaults (see <a class="reference external" href="http://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration">git config ...</a>.). And each
time you use Pyjig to add python source to an existing project, pyjig will add
the source to the repo.</p>
<p>Pyjig will not create the repo is invoked with <code class="docutils literal"><span class="pre">--excludegit</span></code> or of the
dirctory is a subdirectory of an existing git repository. It detects
repository membership by invoking <a class="reference external" href="http://git-scm.com/docs/git-status">git status</a>.</p>
</div>
<div class="section" id="pyjig-name">
<h2>Pyjig Name<a class="headerlink" href="#pyjig-name" title="Permalink to this headline">¶</a></h2>
<p>Pyjig borrows it&#8217;s name from the concept of a jig which is a tool used in metal
and woodworking. A jig is a template that allows one to make duplicates of
pieces.  The simplest example is a key duplication machine, which uses one key
as the guide to make copies.</p>
<div class="section" id="command-line-options">
<h3>Command line options<a class="headerlink" href="#command-line-options" title="Permalink to this headline">¶</a></h3>
<p><em>usage:</em> <code class="docutils literal"><span class="pre">pyjig</span>&nbsp; <span class="pre">[-?]</span> <span class="pre">[-d]</span> <span class="pre">[--pkg</span> <span class="pre">PKG]</span> <span class="pre">[--app</span> <span class="pre">APP]</span> <span class="pre">[-x]</span> <span class="pre">[source</span> <span class="pre">[source</span> <span class="pre">..]]</span></code></p>
<div class="section" id="positional-arguments">
<h4>Positional arguments<a class="headerlink" href="#positional-arguments" title="Permalink to this headline">¶</a></h4>
<dl class="option">
<dt id="cmdoption-arg-source">
<code class="descname">source</code><code class="descclassname"></code><a class="headerlink" href="#cmdoption-arg-source" title="Permalink to this definition">¶</a></dt>
<dd><p>Add one or more source file(s) to project. If the current directry is not part of an
existing project, the source file will be created, but no project related activities
will be taken (no unittest generation, no sphix-docs generation, not added to git...)</p>
</dd></dl>

</div>
<div class="section" id="optional-argument">
<h4>Optional argument:<a class="headerlink" href="#optional-argument" title="Permalink to this headline">¶</a></h4>
<dl class="option">
<dt id="cmdoption-arg-?">
<span id="cmdoption-h"></span><span id="cmdoption--help"></span><code class="descname">?</code><code class="descclassname"></code><code class="descclassname">, </code><code class="descname">-h</code><code class="descclassname"></code><code class="descclassname">, </code><code class="descname">--help</code><code class="descclassname"></code><a class="headerlink" href="#cmdoption-arg-?" title="Permalink to this definition">¶</a></dt>
<dd><p>Display help and exit</p>
</dd></dl>

<dl class="option">
<dt id="cmdoption-d">
<span id="cmdoption--debug"></span><code class="descname">-d</code><code class="descclassname"></code><code class="descclassname">, </code><code class="descname">--debug</code><code class="descclassname"></code><a class="headerlink" href="#cmdoption-d" title="Permalink to this definition">¶</a></dt>
<dd><p>Generate diagnotic output.</p>
</dd></dl>

<dl class="option">
<dt id="cmdoption--pkg">
<code class="descname">--pkg</code><code class="descclassname"> PKG</code><a class="headerlink" href="#cmdoption--pkg" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a distutils package project.</p>
</dd></dl>

<dl class="option">
<dt id="cmdoption--app">
<code class="descname">--app</code><code class="descclassname"> APP</code><a class="headerlink" href="#cmdoption--app" title="Permalink to this definition">¶</a></dt>
<dd><p>Create an application type project.</p>
</dd></dl>

<dl class="option">
<dt id="cmdoption-x">
<span id="cmdoption--excludegit"></span><code class="descname">-x</code><code class="descclassname"></code><code class="descclassname">, </code><code class="descname">--excludegit</code><code class="descclassname"></code><a class="headerlink" href="#cmdoption-x" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not initialize git repo and do not add new source to git repo.</p>
</dd></dl>

</div>
</div>
</div>
</div>
<p>Contents:</p>
<div class="toctree-wrapper compound">
<ul class="simple">
</ul>
</div>
<div class="section" id="indices-and-tables">
<h1>Indices and tables<a class="headerlink" href="#indices-and-tables" title="Permalink to this headline">¶</a></h1>
<ul class="simple">
<li><a class="reference internal" href="genindex.html"><span>Index</span></a></li>
<li><a class="reference internal" href="py-modindex.html"><span>Module Index</span></a></li>
<li><a class="reference internal" href="search.html"><span>Search Page</span></a></li>
</ul>
</div>


          </div>
        </div>
      </div>
      <div class="clearer"></div>
    </div>
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="genindex.html" title="General Index"
             >index</a></li>
        <li class="right" >
          <a href="py-modindex.html" title="Python Module Index"
             >modules</a> |</li>
        <li class="nav-item nav-item-0"><a href="#">Pyjig 1.0.1 documentation</a> &raquo;</li> 
      </ul>
    </div>
    <div class="footer" role="contentinfo">
        &copy; Copyright Copyright(c) 2015, Carroll-Net, Inc., All Rights Reserved.
      Created using <a href="http://sphinx-doc.org/">Sphinx</a> 1.3.1.
    </div>
  </body>
</html>