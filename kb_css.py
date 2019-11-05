""" kb_css.py: Stylesheet tbv. HTML template voor het kanbanpy Kanbanboard
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 05 nov 2019
"""

STYLES = """
body {
  width: 100%;
  background-color: #E0E0E0;
}

h2 {
  margin-left: 5px;
  font-family: 'Arbutus Slab', serif;
  color: #607D8B;
}

ol.kanban {
  width: 20%;
  height: auto;
  margin: 1%;
  max-width: 300px;
  min-width: 200px;
  display: inline-block;
  vertical-align: top;
  box-shadow: 0 2px 2px 0 rgba(0, 0, 0, .14), 0 3px 1px -2px rgba(0, 0, 0, .2), 0 1px 5px 0 rgba(0, 0, 0, .12);
  flex-direction: column;
  min-height: 200px;
  z-index: 1;
  position: relative;
  background: #fff;
  padding: 1em;
  border-radius: 2px;
}

ol.kanban.backlog {
  border-top: 5px solid #FF3D00;
}

ol.kanban.todo {
  border-top: 5px solid #FFB300;
}

ol.kanban.doing {
  border-top: 5px solid #29B6F6;
}

ol.kanban.done {
  border-top: 5px solid #8BC34A;
}

.dd {
  max-width: 100%;
  top: 40px;
  margin: 0 auto;
  display: block;
  vertical-align: top;
  position: relative;
  list-style: none;
}

.dd-item {
  list-style: none;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  min-height: 48px;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-flex-direction: column;
  -ms-flex-direction: column;
  flex-direction: column;
  font-size: 16px;
  min-height: 120px;
  overflow: hidden;
  z-index: 1;
  position: relative;
  background: #fafafa;
  border-radius: 6px;
  margin: 5px 0;
  padding: 5px 10px;
  color: #333;
  text-decoration: none;
  font-weight: bold;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

.dd-item:hover {
  color: #00838F;
  will-change: box-shadow;
  transition: box-shadow .2s cubic-bezier(.4, 0, 1, 1), background-color .2s cubic-bezier(.4, 0, .2, 1), color .2s cubic-bezier(.4, 0, .2, 1);
  box-shadow: 0 5px 6px 0 rgba(0, 0, 0, .14), 0 3px 1px -6px rgba(0, 0, 0, .2), 2px 5px 3px 0 rgba(0, 0, 0, .12);
  background: #fff;
}

.card_title {
  color: inherit;
  display: block;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  font-size: 20px;
  line-height: normal;
  overflow: hidden;
  -webkit-transform-origin: 149px 48px;
  transform-origin: 149px 48px;
  margin: 0;
}

.card_text {
  color: grey;
  border-top: 1px solid font-size: 1rem;
  font-weight: 400;
  line-height: 18px;
  overflow: hidden;
  padding: 16px;
  width: 90%;
}

.card_footer {
  border-top: 1px solid rgba(0, 0, 0, .1);
  font-size: 10px;
  line-height: normal;
  width: 100%;
  color: #B0BEC5;
  padding: 8px;
  box-sizing: border-box;
}
"""