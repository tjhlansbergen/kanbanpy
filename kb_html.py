""" kb_html.py: HTML template voor het kanbanpy Kanbanboard
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 05 nov 2019
"""

SKELETON = """
<html>
<head>
<style>
$CSS
</style>
</head>
<body>

<div class="dd">

<ol class="kanban backlog">
<div class="kanban__title">
<h2>&#9887;<br/>Backlog</h2>
</div>
$BACKLOG	 
</ol>

<ol class="kanban todo">
<div class="kanban__title">
<h2>&star;<br/>Todo</h2>
</div>
$TODO
</ol>

<ol class="kanban doing">
<div class="kanban__title">
<h2>&#9935;<br/>Doing</h2>
</div>
$DOING
</ol>

<ol class="kanban done">
<div class="kanban__title">
<h2>&check;<br/>Done</h2>
</div>
$DONE
</ol>

</div>
</body>
</html>
"""

BLOCK = """
<li class="dd-item" data-id="$ID">
<h3 class="card_title dd-handle" >$ID. $TITLE</h3>
<div class="card_text">
$DESC
</div>
<div class="card_footer">
<ul>
<li>Team: <i>$TEAM</i></li>
<li>Project: <i>$PROJECT</i></li>
</ul>
</div>
</li>
"""