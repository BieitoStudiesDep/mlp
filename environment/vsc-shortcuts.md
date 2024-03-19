<!-- markdownlint-disable MD007 -->
<!-- cSpell:ignore   -->

# VSC ShortCuts

## Linux

|  uso  | comando                                | system                    | desc                               |
| :---: | -------------------------------------- | ------------------------- | ---------------------------------- |
| 5 ⭐️ | cambiar entre grupos                   | system                    | ctr + 1,2                          |
| 5 ⭐️ | cambiar entre pestañas                 | system                    | ctr + tab                          |
| 5 ⭐️ | cambiar pestañas siguiente             | system                    | ctr + avPág                        |
| 5 ⭐️ | cambiar pestañas anterior              | system                    | ctr + rePág                        |
| 5 ⭐️ | mostrar/ocultar panel lateral          | system                    | ctr + b                            |
| 5 ⭐️ | mostrar/ocultar panel terminal         | system                    | ctr + j                            |
| 5 ⭐️ | abrir archivo por nombre               | system                    | ctr + e                            |
| 5 ⭐️ | configuración                          | system                    | ctr + ,                            |
| 5 ⭐️ | Markdown mostrar origen                | system                    | shift + alt + o                    |
| 5 ⭐️ | Markdown mostrar preview               | system                    | shift + alt + o                    |
| 5 ⭐️ | Markdown mostrar preview panel lateral | system                    | ctr + shift + alt + o              |
| 5 ⭐️ | Markdown mostrar preview panel lateral | system                    | ctr + shift + alt + o              |
| 5 ⭐️ | Markdown mostrar preview               | Markdown Preview Enhanced | ctr + shift + alt + m              |
| 5 ⭐️ | Markdown mostrar preview panel lateral | Markdown Preview Enhanced | ctr + shift + alt + m              |
| 5 ⭐️ | editor mover linea                     | editor                    | alt + ⬆️ / alt + ⬇️                |
| 5 ⭐️ | Markdown mostrar preview panel lateral | Markdown Preview Enhanced | ctr + shift + alt + m              |
| 5 ⭐️ | duplicar linea arriba                  | editor                    | shift + alt + ⬇️                   |
| 5 ⭐️ | duplicar linea abajo                   | editor                    | shift + alt + ⬆️                   |
| 5 ⭐️ | duplicar linea de arriba               | editor                    | ctr + d                            |
| 5 ⭐️ | editor agregar cursor abajo            | editor                    | ctr + shift + ⬇️                   |
| 5 ⭐️ | editor agregar cursor arriba           | editor                    | ctr + shift + ⬆️                   |
| 5 ⭐️ | insertar linea abajo                   | editor                    | alt + enter                        |
| 5 ⭐️ | seleccionar todas las coincidencias    | editor                    | ctr + shift + L                    |
| 5 ⭐️ | eliminar linea                         | editor                    | shift + d                          |
| 5 ⭐️ | guardar                                | editor                    | ctr + s                            |
| 5 ⭐️ | guardar todo                           | editor                    | shift + alt + s                    |
| 5 ⭐️ | buscar archivo por nombre              | editor                    | ctr+p                              |
| 5 ⭐️ | comentario de linea                    | editor                    | ctr+ 7 </br>ctr + /                |
| 5 ⭐️ | comentario de bloque                   | editor                    | ctr+ shift + 7 </br>ctr+ shift + / |
| 5 ⭐️ | volver a la pestaña anterior           | system                    | ctr+ alt +-                        |

## ShortCuts Config

```json
// Coloque sus atajos de teclado en este archivo para sobreescribir los valores predeterminadosauto[]
[
  {
    "key": "ctrl+alt+u",
    "command": "editor.action.transformToUppercase"
  },
  {
    "key": "ctrl+alt+l",
    "command": "editor.action.transformToLowercase"
  },
  {
    "key": "shift+alt+o",
    "command": "markdown.showSource"
  },
  {
    "key": "shift+alt+o",
    "command": "markdown.showPreview",
    "when": "!notebookEditorFocused && editorLangId == 'markdown'"
  },
  {
    "key": "ctrl+shift+v",
    "command": "-markdown.showPreview",
    "when": "!notebookEditorFocused && editorLangId == 'markdown'"
  },
  {
    "key": "ctrl+shift+alt+o",
    "command": "markdown.showPreviewToSide",
    "when": "!notebookEditorFocused && editorLangId == 'markdown'"
  },
  {
    "key": "ctrl+k v",
    "command": "-markdown.showPreviewToSide",
    "when": "!notebookEditorFocused && editorLangId == 'markdown'"
  },
  {
    "key": "ctrl+shift+alt+o",
    "command": "markdown.extension.closePreview",
    "when": "activeWebviewPanelId == 'markdown.preview'"
  },
  {
    "key": "ctrl+shift+v",
    "command": "-markdown.extension.closePreview",
    "when": "activeWebviewPanelId == 'markdown.preview'"
  },
  {
    "key": "ctrl+k v",
    "command": "-markdown.extension.closePreview",
    "when": "activeWebviewPanelId == 'markdown.preview'"
  },
  {
    "key": "ctrl+alt+m",
    "command": "markdown-preview-enhanced.openPreview",
    "when": "editorLangId == 'markdown'"
  },
  {
    "key": "ctrl+shift+v",
    "command": "-markdown-preview-enhanced.openPreview",
    "when": "editorLangId == 'markdown'"
  },
  {
    "key": "ctrl+shift+alt+m",
    "command": "markdown-preview-enhanced.openPreviewToTheSide",
    "when": "editorLangId == 'markdown'"
  },
  {
    "key": "ctrl+k v",
    "command": "-markdown-preview-enhanced.openPreviewToTheSide",
    "when": "editorLangId == 'markdown'"
  },
  {
    "key": "alt+down",
    "command": "editor.action.moveLinesDownAction",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "shift+alt+down",
    "command": "-editor.action.moveLinesDownAction",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+shift+down",
    "command": "-editor.action.moveLinesDownAction",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+shift+down",
    "command": "editor.action.insertCursorBelow",
    "when": "editorTextFocus"
  },
  {
    "key": "shift+alt+down",
    "command": "-editor.action.insertCursorBelow",
    "when": "editorTextFocus"
  },
  {
    "key": "shift+alt+down",
    "command": "editor.action.copyLinesDownAction",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+shift+alt+down",
    "command": "-editor.action.copyLinesDownAction",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "shift+alt+down",
    "command": "editor.action.copyLinesDownAction",
    "when": "editorTextFocus && !editorHasSelection && !editorReadonly"
  },
  {
    "key": "ctrl+d",
    "command": "-editor.action.copyLinesDownAction",
    "when": "editorTextFocus && !editorHasSelection && !editorReadonly"
  },
  {
    "key": "shift+alt+up",
    "command": "editor.action.copyLinesUpAction",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+shift+alt+up",
    "command": "-editor.action.copyLinesUpAction",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "alt+enter",
    "command": "editor.action.insertLineAfter",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+enter",
    "command": "-editor.action.insertLineAfter",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+shift+up",
    "command": "editor.action.insertCursorAbove",
    "when": "editorTextFocus"
  },
  {
    "key": "shift+alt+up",
    "command": "-editor.action.insertCursorAbove",
    "when": "editorTextFocus"
  },
  {
    "key": "alt+up",
    "command": "editor.action.moveLinesUpAction",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "shift+alt+up",
    "command": "-editor.action.moveLinesUpAction",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "alt+d",
    "command": "editor.action.deleteLines",
    "when": "textInputFocus && !editorReadonly"
  },
  {
    "key": "ctrl+shift+k",
    "command": "-editor.action.deleteLines",
    "when": "textInputFocus && !editorReadonly"
  },
  {
    "key": "alt+d",
    "command": "editor.action.deleteLines",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+y",
    "command": "-editor.action.deleteLines",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "shift+alt+s",
    "command": "workbench.action.files.saveAll"
  },
  {
    "key": "ctrl+s",
    "command": "-workbench.action.files.saveAll"
  },
  {
    "key": "ctrl+7",
    "command": "editor.action.commentLine",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+-",
    "command": "-editor.action.commentLine",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+numpad_divide",
    "command": "editor.action.commentLine",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+numpad_divide",
    "command": "editor.action.addCommentLine",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+k ctrl+c",
    "command": "-editor.action.addCommentLine",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+shift+7",
    "command": "editor.action.blockComment",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+shift+a",
    "command": "-editor.action.blockComment",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+shift+-",
    "command": "-editor.action.blockComment",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+shift+7",
    "command": "-editor.action.commentLine",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+7",
    "command": "workbench.action.addComment"
  },
  {
    "key": "ctrl+k ctrl+alt+c",
    "command": "-workbench.action.addComment"
  }
]
```
