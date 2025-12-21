<!DOCTYPE html>

<html lang="en">
<head><meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>025-assignment</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script><script>
(function() {
  function addWidgetsRenderer() {
    var mimeElement = document.querySelector('script[type="application/vnd.jupyter.widget-view+json"]');
    var scriptElement = document.createElement('script');
    
    var widgetRendererSrc = 'https://unpkg.com/@jupyter-widgets/html-manager@*/dist/embed-amd.js';
    
    var widgetState;

    // Fallback for older version:
    try {
      widgetState = mimeElement && JSON.parse(mimeElement.innerHTML);

      if (widgetState && (widgetState.version_major < 2 || !widgetState.version_major)) {
        
        var widgetRendererSrc = 'https://unpkg.com/@jupyter-js-widgets@*/dist/embed.js';
        
      }
    } catch(e) {}

    scriptElement.src = widgetRendererSrc;
    document.body.appendChild(scriptElement);
  }

  document.addEventListener('DOMContentLoaded', addWidgetsRenderer);
}());
</script>
<style type="text/css">
    pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: var(--jp-cell-editor-active-background) }
.highlight { background: var(--jp-cell-editor-background); color: var(--jp-mirror-editor-variable-color) }
.highlight .c { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment */
.highlight .err { color: var(--jp-mirror-editor-error-color) } /* Error */
.highlight .k { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword */
.highlight .o { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator */
.highlight .p { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation */
.highlight .ch { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Multiline */
.highlight .cp { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Preproc */
.highlight .cpf { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Single */
.highlight .cs { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Special */
.highlight .kc { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Pseudo */
.highlight .kr { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Type */
.highlight .m { color: var(--jp-mirror-editor-number-color) } /* Literal.Number */
.highlight .s { color: var(--jp-mirror-editor-string-color) } /* Literal.String */
.highlight .ow { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator.Word */
.highlight .pm { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation.Marker */
.highlight .w { color: var(--jp-mirror-editor-variable-color) } /* Text.Whitespace */
.highlight .mb { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Bin */
.highlight .mf { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Float */
.highlight .mh { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Hex */
.highlight .mi { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer */
.highlight .mo { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Oct */
.highlight .sa { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Affix */
.highlight .sb { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Backtick */
.highlight .sc { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Char */
.highlight .dl { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Delimiter */
.highlight .sd { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Doc */
.highlight .s2 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Double */
.highlight .se { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Escape */
.highlight .sh { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Heredoc */
.highlight .si { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Interpol */
.highlight .sx { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Other */
.highlight .sr { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Regex */
.highlight .s1 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Single */
.highlight .ss { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Symbol */
.highlight .il { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer.Long */
  </style>
<style type="text/css">
    #top-panel-wrapper {
  display: none;
}

#menu-panel-wrapper,
#main-panel {
  position: relative !important;
  top: 0px !important;
}

#menu-panel-wrapper #menu-panel #jp-MainMenu .lm-MenuBar-content li:nth-child(1),
#menu-panel-wrapper #menu-panel #jp-MainMenu .lm-MenuBar-content li:nth-child(2),
#menu-panel-wrapper #menu-panel #jp-MainMenu .lm-MenuBar-content li:nth-child(3) {
  display: none;
}

.jp-NotebookTrustedStatus {
  display: none !important;
}

.jp-nb-interface-switcher-button,
[data-command="jupyter-notebook:open-lab"],
[data-command="jupyter-notebook:launch-tree"],
[data-command="application:open-tree"],
[data-command="docmanager:download"] {
  display: none !important;
}

  </style>
<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
 * Mozilla scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */
[data-jp-theme-scrollbars='true'] {
  scrollbar-color: rgb(var(--jp-scrollbar-thumb-color))
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar. These selectors
 * will match lower in the tree, and so will override the above */
[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
  scrollbar-width: thin;
}

/* tiny scrollbar */

.jp-scrollbar-tiny::-webkit-scrollbar,
.jp-scrollbar-tiny::-webkit-scrollbar-corner {
  background-color: transparent;
  height: 4px;
  width: 4px;
}

.jp-scrollbar-tiny::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:horizontal {
  border-left: 0 solid transparent;
  border-right: 0 solid transparent;
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:vertical {
  border-top: 0 solid transparent;
  border-bottom: 0 solid transparent;
}

/*
 * Lumino
 */

.lm-ScrollBar[data-orientation='horizontal'] {
  min-height: 16px;
  max-height: 16px;
  min-width: 45px;
  border-top: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] {
  min-width: 16px;
  max-width: 16px;
  min-height: 45px;
  border-left: 1px solid #a0a0a0;
}

.lm-ScrollBar-button {
  background-color: #f0f0f0;
  background-position: center center;
  min-height: 15px;
  max-height: 15px;
  min-width: 15px;
  max-width: 15px;
}

.lm-ScrollBar-button:hover {
  background-color: #dadada;
}

.lm-ScrollBar-button.lm-mod-active {
  background-color: #cdcdcd;
}

.lm-ScrollBar-track {
  background: #f0f0f0;
}

.lm-ScrollBar-thumb {
  background: #cdcdcd;
}

.lm-ScrollBar-thumb:hover {
  background: #bababa;
}

.lm-ScrollBar-thumb.lm-mod-active {
  background: #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal'] .lm-ScrollBar-thumb {
  height: 100%;
  min-width: 15px;
  border-left: 1px solid #a0a0a0;
  border-right: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] .lm-ScrollBar-thumb {
  width: 100%;
  min-height: 15px;
  border-top: 1px solid #a0a0a0;
  border-bottom: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-left);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-right);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-up);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-down);
  background-size: 17px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
}

.lm-Widget.lm-mod-hidden {
  display: none !important;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.lm-AccordionPanel[data-orientation='horizontal'] > .lm-AccordionPanel-title {
  /* Title is rotated for horizontal accordion panel using CSS */
  display: block;
  transform-origin: top left;
  transform: rotate(-90deg) translate(-100%);
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-CommandPalette-search {
  flex: 0 0 auto;
}

.lm-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}

.lm-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-CommandPalette-item {
  display: flex;
  flex-direction: row;
}

.lm-CommandPalette-itemIcon {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}

.lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-close-icon {
  border: 1px solid transparent;
  background-color: transparent;
  position: absolute;
  z-index: 1;
  right: 3%;
  top: 0;
  bottom: 0;
  margin: auto;
  padding: 7px 0;
  display: none;
  vertical-align: middle;
  outline: 0;
  cursor: pointer;
}
.lm-close-icon:after {
  content: 'X';
  display: block;
  width: 15px;
  height: 15px;
  text-align: center;
  color: #000;
  font-weight: normal;
  font-size: 12px;
  cursor: pointer;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-DockPanel {
  z-index: 0;
}

.lm-DockPanel-widget {
  z-index: 0;
}

.lm-DockPanel-tabBar {
  z-index: 1;
}

.lm-DockPanel-handle {
  z-index: 2;
}

.lm-DockPanel-handle.lm-mod-hidden {
  display: none !important;
}

.lm-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

.lm-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}

.lm-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}

.lm-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

.lm-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

.lm-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}

.lm-DockPanel-overlay.lm-mod-hidden {
  display: none !important;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}

.lm-Menu-item {
  display: table-row;
}

.lm-Menu-item.lm-mod-hidden,
.lm-Menu-item.lm-mod-collapsed {
  display: none !important;
}

.lm-Menu-itemIcon,
.lm-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}

.lm-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}

.lm-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}

.lm-MenuBar-item {
  box-sizing: border-box;
}

.lm-MenuBar-itemIcon,
.lm-MenuBar-itemLabel {
  display: inline-block;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}

.lm-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}

.lm-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}

.lm-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}

.lm-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-SplitPanel-child {
  z-index: 0;
}

.lm-SplitPanel-handle {
  z-index: 1;
}

.lm-SplitPanel-handle.lm-mod-hidden {
  display: none !important;
}

.lm-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle {
  cursor: ew-resize;
}

.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle {
  cursor: ns-resize;
}

.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
  align-items: flex-end;
}

.lm-TabBar[data-orientation='vertical'] {
  flex-direction: column;
  align-items: flex-end;
}

.lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}

.lm-TabBar[data-orientation='horizontal'] > .lm-TabBar-content {
  flex-direction: row;
}

.lm-TabBar[data-orientation='vertical'] > .lm-TabBar-content {
  flex-direction: column;
}

.lm-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
  touch-action: none; /* Disable native Drag/Drop */
}

.lm-TabBar-tabIcon,
.lm-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}

.lm-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}

.lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
}

.lm-TabBar-tab.lm-mod-hidden {
  display: none !important;
}

.lm-TabBar-addButton.lm-mod-hidden {
  display: none !important;
}

.lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
  position: relative;
}

.lm-TabBar.lm-mod-dragging[data-orientation='horizontal'] .lm-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}

.lm-TabBar.lm-mod-dragging[data-orientation='vertical'] .lm-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}

.lm-TabBar.lm-mod-dragging .lm-TabBar-tab.lm-mod-dragging {
  transition: none;
}

.lm-TabBar-tabLabel .lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
  background: inherit;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-TabPanel-tabBar {
  z-index: 1;
}

.lm-TabPanel-stackedPanel {
  z-index: 0;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapse {
  display: flex;
  flex-direction: column;
  align-items: stretch;
}

.jp-Collapse-header {
  padding: 1px 12px;
  background-color: var(--jp-layout-color1);
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  align-items: center;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  text-transform: uppercase;
  user-select: none;
}

.jp-Collapser-icon {
  height: 16px;
}

.jp-Collapse-header-collapsed .jp-Collapser-icon {
  transform: rotate(-90deg);
  margin: auto 0;
}

.jp-Collapser-title {
  line-height: 25px;
}

.jp-Collapse-contents {
  padding: 0 12px;
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensureUiComponents() in @jupyterlab/buildutils */

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

/* Icons urls */

:root {
  --jp-icon-add-above: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5MikiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik00Ljc1IDQuOTMwNjZINi42MjVWNi44MDU2NkM2LjYyNSA3LjAxMTkxIDYuNzkzNzUgNy4xODA2NiA3IDcuMTgwNjZDNy4yMDYyNSA3LjE4MDY2IDcuMzc1IDcuMDExOTEgNy4zNzUgNi44MDU2NlY0LjkzMDY2SDkuMjVDOS40NTYyNSA0LjkzMDY2IDkuNjI1IDQuNzYxOTEgOS42MjUgNC41NTU2NkM5LjYyNSA0LjM0OTQxIDkuNDU2MjUgNC4xODA2NiA5LjI1IDQuMTgwNjZINy4zNzVWMi4zMDU2NkM3LjM3NSAyLjA5OTQxIDcuMjA2MjUgMS45MzA2NiA3IDEuOTMwNjZDNi43OTM3NSAxLjkzMDY2IDYuNjI1IDIuMDk5NDEgNi42MjUgMi4zMDU2NlY0LjE4MDY2SDQuNzVDNC41NDM3NSA0LjE4MDY2IDQuMzc1IDQuMzQ5NDEgNC4zNzUgNC41NTU2NkM0LjM3NSA0Ljc2MTkxIDQuNTQzNzUgNC45MzA2NiA0Ljc1IDQuOTMwNjZaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC43Ii8+CjwvZz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTExLjUgOS41VjExLjVMMi41IDExLjVWOS41TDExLjUgOS41Wk0xMiA4QzEyLjU1MjMgOCAxMyA4LjQ0NzcyIDEzIDlWMTJDMTMgMTIuNTUyMyAxMi41NTIzIDEzIDEyIDEzTDIgMTNDMS40NDc3MiAxMyAxIDEyLjU1MjMgMSAxMlY5QzEgOC40NDc3MiAxLjQ0NzcxIDggMiA4TDEyIDhaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5MiI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KC0xIDAgMCAxIDEwIDEuNTU1NjYpIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==);
  --jp-icon-add-below: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5OCkiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik05LjI1IDEwLjA2OTNMNy4zNzUgMTAuMDY5M0w3LjM3NSA4LjE5NDM0QzcuMzc1IDcuOTg4MDkgNy4yMDYyNSA3LjgxOTM0IDcgNy44MTkzNEM2Ljc5Mzc1IDcuODE5MzQgNi42MjUgNy45ODgwOSA2LjYyNSA4LjE5NDM0TDYuNjI1IDEwLjA2OTNMNC43NSAxMC4wNjkzQzQuNTQzNzUgMTAuMDY5MyA0LjM3NSAxMC4yMzgxIDQuMzc1IDEwLjQ0NDNDNC4zNzUgMTAuNjUwNiA0LjU0Mzc1IDEwLjgxOTMgNC43NSAxMC44MTkzTDYuNjI1IDEwLjgxOTNMNi42MjUgMTIuNjk0M0M2LjYyNSAxMi45MDA2IDYuNzkzNzUgMTMuMDY5MyA3IDEzLjA2OTNDNy4yMDYyNSAxMy4wNjkzIDcuMzc1IDEyLjkwMDYgNy4zNzUgMTIuNjk0M0w3LjM3NSAxMC44MTkzTDkuMjUgMTAuODE5M0M5LjQ1NjI1IDEwLjgxOTMgOS42MjUgMTAuNjUwNiA5LjYyNSAxMC40NDQzQzkuNjI1IDEwLjIzODEgOS40NTYyNSAxMC4wNjkzIDkuMjUgMTAuMDY5M1oiIGZpbGw9IiM2MTYxNjEiIHN0cm9rZT0iIzYxNjE2MSIgc3Ryb2tlLXdpZHRoPSIwLjciLz4KPC9nPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMi41IDUuNUwyLjUgMy41TDExLjUgMy41TDExLjUgNS41TDIuNSA1LjVaTTIgN0MxLjQ0NzcyIDcgMSA2LjU1MjI4IDEgNkwxIDNDMSAyLjQ0NzcyIDEuNDQ3NzIgMiAyIDJMMTIgMkMxMi41NTIzIDIgMTMgMi40NDc3MiAxMyAzTDEzIDZDMTMgNi41NTIyOSAxMi41NTIzIDcgMTIgN0wyIDdaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5OCI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KDEgMS43NDg0NmUtMDcgMS43NDg0NmUtMDcgLTEgNCAxMy40NDQzKSIvPgo8L2NsaXBQYXRoPgo8L2RlZnM+Cjwvc3ZnPgo=);
  --jp-icon-add: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDEzaC02djZoLTJ2LTZINXYtMmg2VjVoMnY2aDZ2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bell: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE2IDE2IiB2ZXJzaW9uPSIxLjEiPgogICA8cGF0aCBjbGFzcz0ianAtaWNvbjIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzMzMzMzIgogICAgICBkPSJtOCAwLjI5Yy0xLjQgMC0yLjcgMC43My0zLjYgMS44LTEuMiAxLjUtMS40IDMuNC0xLjUgNS4yLTAuMTggMi4yLTAuNDQgNC0yLjMgNS4zbDAuMjggMS4zaDVjMC4wMjYgMC42NiAwLjMyIDEuMSAwLjcxIDEuNSAwLjg0IDAuNjEgMiAwLjYxIDIuOCAwIDAuNTItMC40IDAuNi0xIDAuNzEtMS41aDVsMC4yOC0xLjNjLTEuOS0wLjk3LTIuMi0zLjMtMi4zLTUuMy0wLjEzLTEuOC0wLjI2LTMuNy0xLjUtNS4yLTAuODUtMS0yLjItMS44LTMuNi0xLjh6bTAgMS40YzAuODggMCAxLjkgMC41NSAyLjUgMS4zIDAuODggMS4xIDEuMSAyLjcgMS4yIDQuNCAwLjEzIDEuNyAwLjIzIDMuNiAxLjMgNS4yaC0xMGMxLjEtMS42IDEuMi0zLjQgMS4zLTUuMiAwLjEzLTEuNyAwLjMtMy4zIDEuMi00LjQgMC41OS0wLjcyIDEuNi0xLjMgMi41LTEuM3ptLTAuNzQgMTJoMS41Yy0wLjAwMTUgMC4yOCAwLjAxNSAwLjc5LTAuNzQgMC43OS0wLjczIDAuMDAxNi0wLjcyLTAuNTMtMC43NC0wLjc5eiIgLz4KPC9zdmc+Cg==);
  --jp-icon-bug-dot: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiPgogICAgICAgIDxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTcuMTkgOEgyMFYxMEgxNy45MUMxNy45NiAxMC4zMyAxOCAxMC42NiAxOCAxMVYxMkgyMFYxNEgxOC41SDE4VjE0LjAyNzVDMTUuNzUgMTQuMjc2MiAxNCAxNi4xODM3IDE0IDE4LjVDMTQgMTkuMjA4IDE0LjE2MzUgMTkuODc3OSAxNC40NTQ5IDIwLjQ3MzlDMTMuNzA2MyAyMC44MTE3IDEyLjg3NTcgMjEgMTIgMjFDOS43OCAyMSA3Ljg1IDE5Ljc5IDYuODEgMThINFYxNkg2LjA5QzYuMDQgMTUuNjcgNiAxNS4zNCA2IDE1VjE0SDRWMTJINlYxMUM2IDEwLjY2IDYuMDQgMTAuMzMgNi4wOSAxMEg0VjhINi44MUM3LjI2IDcuMjIgNy44OCA2LjU1IDguNjIgNi4wNEw3IDQuNDFMOC40MSAzTDEwLjU5IDUuMTdDMTEuMDQgNS4wNiAxMS41MSA1IDEyIDVDMTIuNDkgNSAxMi45NiA1LjA2IDEzLjQyIDUuMTdMMTUuNTkgM0wxNyA0LjQxTDE1LjM3IDYuMDRDMTYuMTIgNi41NSAxNi43NCA3LjIyIDE3LjE5IDhaTTEwIDE2SDE0VjE0SDEwVjE2Wk0xMCAxMkgxNFYxMEgxMFYxMloiIGZpbGw9IiM2MTYxNjEiLz4KICAgICAgICA8cGF0aCBkPSJNMjIgMTguNUMyMiAyMC40MzMgMjAuNDMzIDIyIDE4LjUgMjJDMTYuNTY3IDIyIDE1IDIwLjQzMyAxNSAxOC41QzE1IDE2LjU2NyAxNi41NjcgMTUgMTguNSAxNUMyMC40MzMgMTUgMjIgMTYuNTY3IDIyIDE4LjVaIiBmaWxsPSIjNjE2MTYxIi8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bug: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yMCA4aC0yLjgxYy0uNDUtLjc4LTEuMDctMS40NS0xLjgyLTEuOTZMMTcgNC40MSAxNS41OSAzbC0yLjE3IDIuMTdDMTIuOTYgNS4wNiAxMi40OSA1IDEyIDVjLS40OSAwLS45Ni4wNi0xLjQxLjE3TDguNDEgMyA3IDQuNDFsMS42MiAxLjYzQzcuODggNi41NSA3LjI2IDcuMjIgNi44MSA4SDR2MmgyLjA5Yy0uMDUuMzMtLjA5LjY2LS4wOSAxdjFINHYyaDJ2MWMwIC4zNC4wNC42Ny4wOSAxSDR2MmgyLjgxYzEuMDQgMS43OSAyLjk3IDMgNS4xOSAzczQuMTUtMS4yMSA1LjE5LTNIMjB2LTJoLTIuMDljLjA1LS4zMy4wOS0uNjYuMDktMXYtMWgydi0yaC0ydi0xYzAtLjM0LS4wNC0uNjctLjA5LTFIMjBWOHptLTYgOGgtNHYtMmg0djJ6bTAtNGgtNHYtMmg0djJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-build: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE0LjkgMTcuNDVDMTYuMjUgMTcuNDUgMTcuMzUgMTYuMzUgMTcuMzUgMTVDMTcuMzUgMTMuNjUgMTYuMjUgMTIuNTUgMTQuOSAxMi41NUMxMy41NCAxMi41NSAxMi40NSAxMy42NSAxMi40NSAxNUMxMi40NSAxNi4zNSAxMy41NCAxNy40NSAxNC45IDE3LjQ1Wk0yMC4xIDE1LjY4TDIxLjU4IDE2Ljg0QzIxLjcxIDE2Ljk1IDIxLjc1IDE3LjEzIDIxLjY2IDE3LjI5TDIwLjI2IDE5LjcxQzIwLjE3IDE5Ljg2IDIwIDE5LjkyIDE5LjgzIDE5Ljg2TDE4LjA5IDE5LjE2QzE3LjczIDE5LjQ0IDE3LjMzIDE5LjY3IDE2LjkxIDE5Ljg1TDE2LjY0IDIxLjdDMTYuNjIgMjEuODcgMTYuNDcgMjIgMTYuMyAyMkgxMy41QzEzLjMyIDIyIDEzLjE4IDIxLjg3IDEzLjE1IDIxLjdMMTIuODkgMTkuODVDMTIuNDYgMTkuNjcgMTIuMDcgMTkuNDQgMTEuNzEgMTkuMTZMOS45NjAwMiAxOS44NkM5LjgxMDAyIDE5LjkyIDkuNjIwMDIgMTkuODYgOS41NDAwMiAxOS43MUw4LjE0MDAyIDE3LjI5QzguMDUwMDIgMTcuMTMgOC4wOTAwMiAxNi45NSA4LjIyMDAyIDE2Ljg0TDkuNzAwMDIgMTUuNjhMOS42NTAwMSAxNUw5LjcwMDAyIDE0LjMxTDguMjIwMDIgMTMuMTZDOC4wOTAwMiAxMy4wNSA4LjA1MDAyIDEyLjg2IDguMTQwMDIgMTIuNzFMOS41NDAwMiAxMC4yOUM5LjYyMDAyIDEwLjEzIDkuODEwMDIgMTAuMDcgOS45NjAwMiAxMC4xM0wxMS43MSAxMC44NEMxMi4wNyAxMC41NiAxMi40NiAxMC4zMiAxMi44OSAxMC4xNUwxMy4xNSA4LjI4OTk4QzEzLjE4IDguMTI5OTggMTMuMzIgNy45OTk5OCAxMy41IDcuOTk5OThIMTYuM0MxNi40NyA3Ljk5OTk4IDE2LjYyIDguMTI5OTggMTYuNjQgOC4yODk5OEwxNi45MSAxMC4xNUMxNy4zMyAxMC4zMiAxNy43MyAxMC41NiAxOC4wOSAxMC44NEwxOS44MyAxMC4xM0MyMCAxMC4wNyAyMC4xNyAxMC4xMyAyMC4yNiAxMC4yOUwyMS42NiAxMi43MUMyMS43NSAxMi44NiAyMS43MSAxMy4wNSAyMS41OCAxMy4xNkwyMC4xIDE0LjMxTDIwLjE1IDE1TDIwLjEgMTUuNjhaIi8+CiAgICA8cGF0aCBkPSJNNy4zMjk2NiA3LjQ0NDU0QzguMDgzMSA3LjAwOTU0IDguMzM5MzIgNi4wNTMzMiA3LjkwNDMyIDUuMjk5ODhDNy40NjkzMiA0LjU0NjQzIDYuNTA4MSA0LjI4MTU2IDUuNzU0NjYgNC43MTY1NkM1LjM5MTc2IDQuOTI2MDggNS4xMjY5NSA1LjI3MTE4IDUuMDE4NDkgNS42NzU5NEM0LjkxMDA0IDYuMDgwNzEgNC45NjY4MiA2LjUxMTk4IDUuMTc2MzQgNi44NzQ4OEM1LjYxMTM0IDcuNjI4MzIgNi41NzYyMiA3Ljg3OTU0IDcuMzI5NjYgNy40NDQ1NFpNOS42NTcxOCA0Ljc5NTkzTDEwLjg2NzIgNC45NTE3OUMxMC45NjI4IDQuOTc3NDEgMTEuMDQwMiA1LjA3MTMzIDExLjAzODIgNS4xODc5M0wxMS4wMzg4IDYuOTg4OTNDMTEuMDQ1NSA3LjEwMDU0IDEwLjk2MTYgNy4xOTUxOCAxMC44NTUgNy4yMTA1NEw5LjY2MDAxIDcuMzgwODNMOS4yMzkxNSA4LjEzMTg4TDkuNjY5NjEgOS4yNTc0NUM5LjcwNzI5IDkuMzYyNzEgOS42NjkzNCA5LjQ3Njk5IDkuNTc0MDggOS41MzE5OUw4LjAxNTIzIDEwLjQzMkM3LjkxMTMxIDEwLjQ5MiA3Ljc5MzM3IDEwLjQ2NzcgNy43MjEwNSAxMC4zODI0TDYuOTg3NDggOS40MzE4OEw2LjEwOTMxIDkuNDMwODNMNS4zNDcwNCAxMC4zOTA1QzUuMjg5MDkgMTAuNDcwMiA1LjE3MzgzIDEwLjQ5MDUgNS4wNzE4NyAxMC40MzM5TDMuNTEyNDUgOS41MzI5M0MzLjQxMDQ5IDkuNDc2MzMgMy4zNzY0NyA5LjM1NzQxIDMuNDEwNzUgOS4yNTY3OUwzLjg2MzQ3IDguMTQwOTNMMy42MTc0OSA3Ljc3NDg4TDMuNDIzNDcgNy4zNzg4M0wyLjIzMDc1IDcuMjEyOTdDMi4xMjY0NyA3LjE5MjM1IDIuMDQwNDkgNy4xMDM0MiAyLjA0MjQ1IDYuOTg2ODJMMi4wNDE4NyA1LjE4NTgyQzIuMDQzODMgNS4wNjkyMiAyLjExOTA5IDQuOTc5NTggMi4yMTcwNCA0Ljk2OTIyTDMuNDIwNjUgNC43OTM5M0wzLjg2NzQ5IDQuMDI3ODhMMy40MTEwNSAyLjkxNzMxQzMuMzczMzcgMi44MTIwNCAzLjQxMTMxIDIuNjk3NzYgMy41MTUyMyAyLjYzNzc2TDUuMDc0MDggMS43Mzc3NkM1LjE2OTM0IDEuNjgyNzYgNS4yODcyOSAxLjcwNzA0IDUuMzU5NjEgMS43OTIzMUw2LjExOTE1IDIuNzI3ODhMNi45ODAwMSAyLjczODkzTDcuNzI0OTYgMS43ODkyMkM3Ljc5MTU2IDEuNzA0NTggNy45MTU0OCAxLjY3OTIyIDguMDA4NzkgMS43NDA4Mkw5LjU2ODIxIDIuNjQxODJDOS42NzAxNyAyLjY5ODQyIDkuNzEyODUgMi44MTIzNCA5LjY4NzIzIDIuOTA3OTdMOS4yMTcxOCA0LjAzMzgzTDkuNDYzMTYgNC4zOTk4OEw5LjY1NzE4IDQuNzk1OTNaIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iOS45LDEzLjYgMy42LDcuNCA0LjQsNi42IDkuOSwxMi4yIDE1LjQsNi43IDE2LjEsNy40ICIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNS45TDksOS43bDMuOC0zLjhsMS4yLDEuMmwtNC45LDVsLTQuOS01TDUuMiw1Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNy41TDksMTEuMmwzLjgtMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-left: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik0xMC44LDEyLjhMNy4xLDlsMy44LTMuOGwwLDcuNkgxMC44eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-right: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik03LjIsNS4yTDEwLjksOWwtMy44LDMuOFY1LjJINy4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-up-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iMTUuNCwxMy4zIDkuOSw3LjcgNC40LDEzLjIgMy42LDEyLjUgOS45LDYuMyAxNi4xLDEyLjYgIi8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-up: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik01LjIsMTAuNUw5LDYuOGwzLjgsMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-case-sensitive: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWFjY2VudDIiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTcuNiw4aDAuOWwzLjUsOGgtMS4xTDEwLDE0SDZsLTAuOSwySDRMNy42LDh6IE04LDkuMUw2LjQsMTNoMy4yTDgsOS4xeiIvPgogICAgPHBhdGggZD0iTTE2LjYsOS44Yy0wLjIsMC4xLTAuNCwwLjEtMC43LDAuMWMtMC4yLDAtMC40LTAuMS0wLjYtMC4yYy0wLjEtMC4xLTAuMi0wLjQtMC4yLTAuNyBjLTAuMywwLjMtMC42LDAuNS0wLjksMC43Yy0wLjMsMC4xLTAuNywwLjItMS4xLDAuMmMtMC4zLDAtMC41LDAtMC43LTAuMWMtMC4yLTAuMS0wLjQtMC4yLTAuNi0wLjNjLTAuMi0wLjEtMC4zLTAuMy0wLjQtMC41IGMtMC4xLTAuMi0wLjEtMC40LTAuMS0wLjdjMC0wLjMsMC4xLTAuNiwwLjItMC44YzAuMS0wLjIsMC4zLTAuNCwwLjQtMC41QzEyLDcsMTIuMiw2LjksMTIuNSw2LjhjMC4yLTAuMSwwLjUtMC4xLDAuNy0wLjIgYzAuMy0wLjEsMC41LTAuMSwwLjctMC4xYzAuMiwwLDAuNC0wLjEsMC42LTAuMWMwLjIsMCwwLjMtMC4xLDAuNC0wLjJjMC4xLTAuMSwwLjItMC4yLDAuMi0wLjRjMC0xLTEuMS0xLTEuMy0xIGMtMC40LDAtMS40LDAtMS40LDEuMmgtMC45YzAtMC40LDAuMS0wLjcsMC4yLTFjMC4xLTAuMiwwLjMtMC40LDAuNS0wLjZjMC4yLTAuMiwwLjUtMC4zLDAuOC0wLjNDMTMuMyw0LDEzLjYsNCwxMy45LDQgYzAuMywwLDAuNSwwLDAuOCwwLjFjMC4zLDAsMC41LDAuMSwwLjcsMC4yYzAuMiwwLjEsMC40LDAuMywwLjUsMC41QzE2LDUsMTYsNS4yLDE2LDUuNnYyLjljMCwwLjIsMCwwLjQsMCwwLjUgYzAsMC4xLDAuMSwwLjIsMC4zLDAuMmMwLjEsMCwwLjIsMCwwLjMsMFY5Ljh6IE0xNS4yLDYuOWMtMS4yLDAuNi0zLjEsMC4yLTMuMSwxLjRjMCwxLjQsMy4xLDEsMy4xLTAuNVY2Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik05IDE2LjE3TDQuODMgMTJsLTEuNDIgMS40MUw5IDE5IDIxIDdsLTEuNDEtMS40MXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-circle-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDJDNi40NyAyIDIgNi40NyAyIDEyczQuNDcgMTAgMTAgMTAgMTAtNC40NyAxMC0xMFMxNy41MyAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4LTggOCAzLjU5IDggOC0zLjU5IDgtOCA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-circle: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iOSIgY3k9IjkiIHI9IjgiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-clear: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8bWFzayBpZD0iZG9udXRIb2xlIj4KICAgIDxyZWN0IHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0id2hpdGUiIC8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSI4IiBmaWxsPSJibGFjayIvPgogIDwvbWFzaz4KCiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxyZWN0IGhlaWdodD0iMTgiIHdpZHRoPSIyIiB4PSIxMSIgeT0iMyIgdHJhbnNmb3JtPSJyb3RhdGUoMzE1LCAxMiwgMTIpIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgbWFzaz0idXJsKCNkb251dEhvbGUpIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-close: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1ub25lIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIGpwLWljb24zLWhvdmVyIiBmaWxsPSJub25lIj4KICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjExIi8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIGpwLWljb24tYWNjZW50Mi1ob3ZlciIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMTkgNi40MUwxNy41OSA1IDEyIDEwLjU5IDYuNDEgNSA1IDYuNDEgMTAuNTkgMTIgNSAxNy41OSA2LjQxIDE5IDEyIDEzLjQxIDE3LjU5IDE5IDE5IDE3LjU5IDEzLjQxIDEyeiIvPgogIDwvZz4KCiAgPGcgY2xhc3M9ImpwLWljb24tbm9uZSBqcC1pY29uLWJ1c3kiIGZpbGw9Im5vbmUiPgogICAgPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiI+CiAgICA8cGF0aCBkPSJNNi41OSwzLjQxTDIsOEw2LjU5LDEyLjZMOCwxMS4xOEw0LjgyLDhMOCw0LjgyTDYuNTksMy40MU0xMi40MSwzLjQxTDExLDQuODJMMTQuMTgsOEwxMSwxMS4xOEwxMi40MSwxMi42TDE3LDhMMTIuNDEsMy40MU0yMS41OSwxMS41OUwxMy41LDE5LjY4TDkuODMsMTZMOC40MiwxNy40MUwxMy41LDIyLjVMMjMsMTNMMjEuNTksMTEuNTlaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTExLjQgMTguNkw2LjggMTRMMTEuNCA5LjRMMTAgOEw0IDE0TDEwIDIwTDExLjQgMTguNlpNMTYuNiAxOC42TDIxLjIgMTRMMTYuNiA5LjRMMTggOEwyNCAxNEwxOCAyMEwxNi42IDE4LjZWMTguNloiLz4KCTwvZz4KPC9zdmc+Cg==);
  --jp-icon-collapse-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNNiAxM3YyaDh2LTJ6IiAvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-console: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwMCAyMDAiPgogIDxnIGNsYXNzPSJqcC1jb25zb2xlLWljb24tYmFja2dyb3VuZC1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMjg4RDEiPgogICAgPHBhdGggZD0iTTIwIDE5LjhoMTYwdjE1OS45SDIweiIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtY29uc29sZS1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIj4KICAgIDxwYXRoIGQ9Ik0xMDUgMTI3LjNoNDB2MTIuOGgtNDB6TTUxLjEgNzdMNzQgOTkuOWwtMjMuMyAyMy4zIDEwLjUgMTAuNSAyMy4zLTIzLjNMOTUgOTkuOSA4NC41IDg5LjQgNjEuNiA2Ni41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copy: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTExLjksMUgzLjJDMi40LDEsMS43LDEuNywxLjcsMi41djEwLjJoMS41VjIuNWg4LjdWMXogTTE0LjEsMy45aC04Yy0wLjgsMC0xLjUsMC43LTEuNSwxLjV2MTAuMmMwLDAuOCwwLjcsMS41LDEuNSwxLjVoOCBjMC44LDAsMS41LTAuNywxLjUtMS41VjUuNEMxNS41LDQuNiwxNC45LDMuOSwxNC4xLDMuOXogTTE0LjEsMTUuNWgtOFY1LjRoOFYxNS41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copyright: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDI0IDI0IiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCI+CiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0xMS44OCw5LjE0YzEuMjgsMC4wNiwxLjYxLDEuMTUsMS42MywxLjY2aDEuNzljLTAuMDgtMS45OC0xLjQ5LTMuMTktMy40NS0zLjE5QzkuNjQsNy42MSw4LDksOCwxMi4xNCBjMCwxLjk0LDAuOTMsNC4yNCwzLjg0LDQuMjRjMi4yMiwwLDMuNDEtMS42NSwzLjQ0LTIuOTVoLTEuNzljLTAuMDMsMC41OS0wLjQ1LDEuMzgtMS42MywxLjQ0QzEwLjU1LDE0LjgzLDEwLDEzLjgxLDEwLDEyLjE0IEMxMCw5LjI1LDExLjI4LDkuMTYsMTEuODgsOS4xNHogTTEyLDJDNi40OCwyLDIsNi40OCwyLDEyczQuNDgsMTAsMTAsMTBzMTAtNC40OCwxMC0xMFMxNy41MiwyLDEyLDJ6IE0xMiwyMGMtNC40MSwwLTgtMy41OS04LTggczMuNTktOCw4LThzOCwzLjU5LDgsOFMxNi40MSwyMCwxMiwyMHoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-cut: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkuNjQgNy42NGMuMjMtLjUuMzYtMS4wNS4zNi0xLjY0IDAtMi4yMS0xLjc5LTQtNC00UzIgMy43OSAyIDZzMS43OSA0IDQgNGMuNTkgMCAxLjE0LS4xMyAxLjY0LS4zNkwxMCAxMmwtMi4zNiAyLjM2QzcuMTQgMTQuMTMgNi41OSAxNCA2IDE0Yy0yLjIxIDAtNCAxLjc5LTQgNHMxLjc5IDQgNCA0IDQtMS43OSA0LTRjMC0uNTktLjEzLTEuMTQtLjM2LTEuNjRMMTIgMTRsNyA3aDN2LTFMOS42NCA3LjY0ek02IDhjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTAgMTJjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTYtNy41Yy0uMjggMC0uNS0uMjItLjUtLjVzLjIyLS41LjUtLjUuNS4yMi41LjUtLjIyLjUtLjUuNXpNMTkgM2wtNiA2IDIgMiA3LTdWM3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-delete: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2cHgiIGhlaWdodD0iMTZweCI+CiAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIiAvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjI2MjYyIiBkPSJNNiAxOWMwIDEuMS45IDIgMiAyaDhjMS4xIDAgMi0uOSAyLTJWN0g2djEyek0xOSA0aC0zLjVsLTEtMWgtNWwtMSAxSDV2MmgxNFY0eiIgLz4KPC9zdmc+Cg==);
  --jp-icon-download: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDloLTRWM0g5djZINWw3IDcgNy03ek01IDE4djJoMTR2LTJINXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-duplicate: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTIuNzk5OTggMC44NzVIOC44OTU4MkM5LjIwMDYxIDAuODc1IDkuNDQ5OTggMS4xMzkxNCA5LjQ0OTk4IDEuNDYxOThDOS40NDk5OCAxLjc4NDgyIDkuMjAwNjEgMi4wNDg5NiA4Ljg5NTgyIDIuMDQ4OTZIMy4zNTQxNUMzLjA0OTM2IDIuMDQ4OTYgMi43OTk5OCAyLjMxMzEgMi43OTk5OCAyLjYzNTk0VjkuNjc5NjlDMi43OTk5OCAxMC4wMDI1IDIuNTUwNjEgMTAuMjY2NyAyLjI0NTgyIDEwLjI2NjdDMS45NDEwMyAxMC4yNjY3IDEuNjkxNjUgMTAuMDAyNSAxLjY5MTY1IDkuNjc5NjlWMi4wNDg5NkMxLjY5MTY1IDEuNDAzMjggMi4xOTA0IDAuODc1IDIuNzk5OTggMC44NzVaTTUuMzY2NjUgMTEuOVY0LjU1SDExLjA4MzNWMTEuOUg1LjM2NjY1Wk00LjE0MTY1IDQuMTQxNjdDNC4xNDE2NSAzLjY5MDYzIDQuNTA3MjggMy4zMjUgNC45NTgzMiAzLjMyNUgxMS40OTE3QzExLjk0MjcgMy4zMjUgMTIuMzA4MyAzLjY5MDYzIDEyLjMwODMgNC4xNDE2N1YxMi4zMDgzQzEyLjMwODMgMTIuNzU5NCAxMS45NDI3IDEzLjEyNSAxMS40OTE3IDEzLjEyNUg0Ljk1ODMyQzQuNTA3MjggMTMuMTI1IDQuMTQxNjUgMTIuNzU5NCA0LjE0MTY1IDEyLjMwODNWNC4xNDE2N1oiIGZpbGw9IiM2MTYxNjEiLz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNOS40MzU3NCA4LjI2NTA3SDguMzY0MzFWOS4zMzY1QzguMzY0MzEgOS40NTQzNSA4LjI2Nzg4IDkuNTUwNzggOC4xNTAwMiA5LjU1MDc4QzguMDMyMTcgOS41NTA3OCA3LjkzNTc0IDkuNDU0MzUgNy45MzU3NCA5LjMzNjVWOC4yNjUwN0g2Ljg2NDMxQzYuNzQ2NDUgOC4yNjUwNyA2LjY1MDAyIDguMTY4NjQgNi42NTAwMiA4LjA1MDc4QzYuNjUwMDIgNy45MzI5MiA2Ljc0NjQ1IDcuODM2NSA2Ljg2NDMxIDcuODM2NUg3LjkzNTc0VjYuNzY1MDdDNy45MzU3NCA2LjY0NzIxIDguMDMyMTcgNi41NTA3OCA4LjE1MDAyIDYuNTUwNzhDOC4yNjc4OCA2LjU1MDc4IDguMzY0MzEgNi42NDcyMSA4LjM2NDMxIDYuNzY1MDdWNy44MzY1SDkuNDM1NzRDOS41NTM2IDcuODM2NSA5LjY1MDAyIDcuOTMyOTIgOS42NTAwMiA4LjA1MDc4QzkuNjUwMDIgOC4xNjg2NCA5LjU1MzYgOC4yNjUwNyA5LjQzNTc0IDguMjY1MDdaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC41Ii8+Cjwvc3ZnPgo=);
  --jp-icon-edit: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMgMTcuMjVWMjFoMy43NUwxNy44MSA5Ljk0bC0zLjc1LTMuNzVMMyAxNy4yNXpNMjAuNzEgNy4wNGMuMzktLjM5LjM5LTEuMDIgMC0xLjQxbC0yLjM0LTIuMzRjLS4zOS0uMzktMS4wMi0uMzktMS40MSAwbC0xLjgzIDEuODMgMy43NSAzLjc1IDEuODMtMS44M3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-ellipses: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iNSIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxOSIgY3k9IjEyIiByPSIyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-error: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjE5IiByPSIyIi8+PHBhdGggZD0iTTEwIDNoNHYxMmgtNHoiLz48L2c+CjxwYXRoIGZpbGw9Im5vbmUiIGQ9Ik0wIDBoMjR2MjRIMHoiLz4KPC9zdmc+Cg==);
  --jp-icon-expand-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNMTEgMTBIOXYzSDZ2MmgzdjNoMnYtM2gzdi0yaC0zeiIgLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-extension: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwLjUgMTFIMTlWN2MwLTEuMS0uOS0yLTItMmgtNFYzLjVDMTMgMi4xMiAxMS44OCAxIDEwLjUgMVM4IDIuMTIgOCAzLjVWNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAydjMuOEgzLjVjMS40OSAwIDIuNyAxLjIxIDIuNyAyLjdzLTEuMjEgMi43LTIuNyAyLjdIMlYyMGMwIDEuMS45IDIgMiAyaDMuOHYtMS41YzAtMS40OSAxLjIxLTIuNyAyLjctMi43IDEuNDkgMCAyLjcgMS4yMSAyLjcgMi43VjIySDE3YzEuMSAwIDItLjkgMi0ydi00aDEuNWMxLjM4IDAgMi41LTEuMTIgMi41LTIuNVMyMS44OCAxMSAyMC41IDExeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-fast-forward: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTQgMThsOC41LTZMNCA2djEyem05LTEydjEybDguNS02TDEzIDZ6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-file-upload: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkgMTZoNnYtNmg0bC03LTctNyA3aDR6bS00IDJoMTR2Mkg1eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-file: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuMyA4LjJsLTUuNS01LjVjLS4zLS4zLS43LS41LTEuMi0uNUgzLjljLS44LjEtMS42LjktMS42IDEuOHYxNC4xYzAgLjkuNyAxLjYgMS42IDEuNmgxNC4yYy45IDAgMS42LS43IDEuNi0xLjZWOS40Yy4xLS41LS4xLS45LS40LTEuMnptLTUuOC0zLjNsMy40IDMuNmgtMy40VjQuOXptMy45IDEyLjdINC43Yy0uMSAwLS4yIDAtLjItLjJWNC43YzAtLjIuMS0uMy4yLS4zaDcuMnY0LjRzMCAuOC4zIDEuMWMuMy4zIDEuMS4zIDEuMS4zaDQuM3Y3LjJzLS4xLjItLjIuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-filter-dot: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWRvdCIgZmlsbD0iI0ZGRiI+CiAgICA8Y2lyY2xlIGN4PSIxOCIgY3k9IjE3IiByPSIzIj48L2NpcmNsZT4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-filter-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEwIDE4aDR2LTJoLTR2MnpNMyA2djJoMThWNkgzem0zIDdoMTJ2LTJINnYyeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-filter: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-folder-favorite: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgwVjB6IiBmaWxsPSJub25lIi8+PHBhdGggY2xhc3M9ImpwLWljb24zIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxNjE2MSIgZD0iTTIwIDZoLThsLTItMkg0Yy0xLjEgMC0yIC45LTIgMnYxMmMwIDEuMS45IDIgMiAyaDE2YzEuMSAwIDItLjkgMi0yVjhjMC0xLjEtLjktMi0yLTJ6bS0yLjA2IDExTDE1IDE1LjI4IDEyLjA2IDE3bC43OC0zLjMzLTIuNTktMi4yNCAzLjQxLS4yOUwxNSA4bDEuMzQgMy4xNCAzLjQxLjI5LTIuNTkgMi4yNC43OCAzLjMzeiIvPgo8L3N2Zz4K);
  --jp-icon-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY4YzAtMS4xLS45LTItMi0yaC04bC0yLTJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-home: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xMCAyMHYtNmg0djZoNXYtOGgzTDEyIDMgMiAxMmgzdjh6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-html5: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMDAiIGQ9Ik0xMDguNCAwaDIzdjIyLjhoMjEuMlYwaDIzdjY5aC0yM1Y0NmgtMjF2MjNoLTIzLjJNMjA2IDIzaC0yMC4zVjBoNjMuN3YyM0gyMjl2NDZoLTIzbTUzLjUtNjloMjQuMWwxNC44IDI0LjNMMzEzLjIgMGgyNC4xdjY5aC0yM1YzNC44bC0xNi4xIDI0LjgtMTYuMS0yNC44VjY5aC0yMi42bTg5LjItNjloMjN2NDYuMmgzMi42VjY5aC01NS42Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2U0NGQyNiIgZD0iTTEwNy42IDQ3MWwtMzMtMzcwLjRoMzYyLjhsLTMzIDM3MC4yTDI1NS43IDUxMiIvPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNmMTY1MjkiIGQ9Ik0yNTYgNDgwLjVWMTMxaDE0OC4zTDM3NiA0NDciLz4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNlYmViZWIiIGQ9Ik0xNDIgMTc2LjNoMTE0djQ1LjRoLTY0LjJsNC4yIDQ2LjVoNjB2NDUuM0gxNTQuNG0yIDIyLjhIMjAybDMuMiAzNi4zIDUwLjggMTMuNnY0Ny40bC05My4yLTI2Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIiBkPSJNMzY5LjYgMTc2LjNIMjU1Ljh2NDUuNGgxMDkuNm0tNC4xIDQ2LjVIMjU1Ljh2NDUuNGg1NmwtNS4zIDU5LTUwLjcgMTMuNnY0Ny4ybDkzLTI1LjgiLz4KPC9zdmc+Cg==);
  --jp-icon-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1icmFuZDQganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNGRkYiIGQ9Ik0yLjIgMi4yaDE3LjV2MTcuNUgyLjJ6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzNGNTFCNSIgZD0iTTIuMiAyLjJ2MTcuNWgxNy41bC4xLTE3LjVIMi4yem0xMi4xIDIuMmMxLjIgMCAyLjIgMSAyLjIgMi4ycy0xIDIuMi0yLjIgMi4yLTIuMi0xLTIuMi0yLjIgMS0yLjIgMi4yLTIuMnpNNC40IDE3LjZsMy4zLTguOCAzLjMgNi42IDIuMi0zLjIgNC40IDUuNEg0LjR6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-info: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUwLjk3OCA1MC45NzgiPgoJPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KCQk8cGF0aCBkPSJNNDMuNTIsNy40NThDMzguNzExLDIuNjQ4LDMyLjMwNywwLDI1LjQ4OSwwQzE4LjY3LDAsMTIuMjY2LDIuNjQ4LDcuNDU4LDcuNDU4CgkJCWMtOS45NDMsOS45NDEtOS45NDMsMjYuMTE5LDAsMzYuMDYyYzQuODA5LDQuODA5LDExLjIxMiw3LjQ1NiwxOC4wMzEsNy40NThjMCwwLDAuMDAxLDAsMC4wMDIsMAoJCQljNi44MTYsMCwxMy4yMjEtMi42NDgsMTguMDI5LTcuNDU4YzQuODA5LTQuODA5LDcuNDU3LTExLjIxMiw3LjQ1Ny0xOC4wM0M1MC45NzcsMTguNjcsNDguMzI4LDEyLjI2Niw0My41Miw3LjQ1OHoKCQkJIE00Mi4xMDYsNDIuMTA1Yy00LjQzMiw0LjQzMS0xMC4zMzIsNi44NzItMTYuNjE1LDYuODcyaC0wLjAwMmMtNi4yODUtMC4wMDEtMTIuMTg3LTIuNDQxLTE2LjYxNy02Ljg3MgoJCQljLTkuMTYyLTkuMTYzLTkuMTYyLTI0LjA3MSwwLTMzLjIzM0MxMy4zMDMsNC40NCwxOS4yMDQsMiwyNS40ODksMmM2LjI4NCwwLDEyLjE4NiwyLjQ0LDE2LjYxNyw2Ljg3MgoJCQljNC40MzEsNC40MzEsNi44NzEsMTAuMzMyLDYuODcxLDE2LjYxN0M0OC45NzcsMzEuNzcyLDQ2LjUzNiwzNy42NzUsNDIuMTA2LDQyLjEwNXoiLz4KCQk8cGF0aCBkPSJNMjMuNTc4LDMyLjIxOGMtMC4wMjMtMS43MzQsMC4xNDMtMy4wNTksMC40OTYtMy45NzJjMC4zNTMtMC45MTMsMS4xMS0xLjk5NywyLjI3Mi0zLjI1MwoJCQljMC40NjgtMC41MzYsMC45MjMtMS4wNjIsMS4zNjctMS41NzVjMC42MjYtMC43NTMsMS4xMDQtMS40NzgsMS40MzYtMi4xNzVjMC4zMzEtMC43MDcsMC40OTUtMS41NDEsMC40OTUtMi41CgkJCWMwLTEuMDk2LTAuMjYtMi4wODgtMC43NzktMi45NzljLTAuNTY1LTAuODc5LTEuNTAxLTEuMzM2LTIuODA2LTEuMzY5Yy0xLjgwMiwwLjA1Ny0yLjk4NSwwLjY2Ny0zLjU1LDEuODMyCgkJCWMtMC4zMDEsMC41MzUtMC41MDMsMS4xNDEtMC42MDcsMS44MTRjLTAuMTM5LDAuNzA3LTAuMjA3LDEuNDMyLTAuMjA3LDIuMTc0aC0yLjkzN2MtMC4wOTEtMi4yMDgsMC40MDctNC4xMTQsMS40OTMtNS43MTkKCQkJYzEuMDYyLTEuNjQsMi44NTUtMi40ODEsNS4zNzgtMi41MjdjMi4xNiwwLjAyMywzLjg3NCwwLjYwOCw1LjE0MSwxLjc1OGMxLjI3OCwxLjE2LDEuOTI5LDIuNzY0LDEuOTUsNC44MTEKCQkJYzAsMS4xNDItMC4xMzcsMi4xMTEtMC40MSwyLjkxMWMtMC4zMDksMC44NDUtMC43MzEsMS41OTMtMS4yNjgsMi4yNDNjLTAuNDkyLDAuNjUtMS4wNjgsMS4zMTgtMS43MywyLjAwMgoJCQljLTAuNjUsMC42OTctMS4zMTMsMS40NzktMS45ODcsMi4zNDZjLTAuMjM5LDAuMzc3LTAuNDI5LDAuNzc3LTAuNTY1LDEuMTk5Yy0wLjE2LDAuOTU5LTAuMjE3LDEuOTUxLTAuMTcxLDIuOTc5CgkJCUMyNi41ODksMzIuMjE4LDIzLjU3OCwzMi4yMTgsMjMuNTc4LDMyLjIxOHogTTIzLjU3OCwzOC4yMnYtMy40ODRoMy4wNzZ2My40ODRIMjMuNTc4eiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-inspector: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaW5zcGVjdG9yLWljb24tY29sb3IganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY2YzAtMS4xLS45LTItMi0yem0tNSAxNEg0di00aDExdjR6bTAtNUg0VjloMTF2NHptNSA1aC00VjloNHY5eiIvPgo8L3N2Zz4K);
  --jp-icon-json: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtanNvbi1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0Y5QTgyNSI+CiAgICA8cGF0aCBkPSJNMjAuMiAxMS44Yy0xLjYgMC0xLjcuNS0xLjcgMSAwIC40LjEuOS4xIDEuMy4xLjUuMS45LjEgMS4zIDAgMS43LTEuNCAyLjMtMy41IDIuM2gtLjl2LTEuOWguNWMxLjEgMCAxLjQgMCAxLjQtLjggMC0uMyAwLS42LS4xLTEgMC0uNC0uMS0uOC0uMS0xLjIgMC0xLjMgMC0xLjggMS4zLTItMS4zLS4yLTEuMy0uNy0xLjMtMiAwLS40LjEtLjguMS0xLjIuMS0uNC4xLS43LjEtMSAwLS44LS40LS43LTEuNC0uOGgtLjVWNC4xaC45YzIuMiAwIDMuNS43IDMuNSAyLjMgMCAuNC0uMS45LS4xIDEuMy0uMS41LS4xLjktLjEgMS4zIDAgLjUuMiAxIDEuNyAxdjEuOHpNMS44IDEwLjFjMS42IDAgMS43LS41IDEuNy0xIDAtLjQtLjEtLjktLjEtMS4zLS4xLS41LS4xLS45LS4xLTEuMyAwLTEuNiAxLjQtMi4zIDMuNS0yLjNoLjl2MS45aC0uNWMtMSAwLTEuNCAwLTEuNC44IDAgLjMgMCAuNi4xIDEgMCAuMi4xLjYuMSAxIDAgMS4zIDAgMS44LTEuMyAyQzYgMTEuMiA2IDExLjcgNiAxM2MwIC40LS4xLjgtLjEgMS4yLS4xLjMtLjEuNy0uMSAxIDAgLjguMy44IDEuNC44aC41djEuOWgtLjljLTIuMSAwLTMuNS0uNi0zLjUtMi4zIDAtLjQuMS0uOS4xLTEuMy4xLS41LjEtLjkuMS0xLjMgMC0uNS0uMi0xLTEuNy0xdi0xLjl6Ii8+CiAgICA8Y2lyY2xlIGN4PSIxMSIgY3k9IjEzLjgiIHI9IjIuMSIvPgogICAgPGNpcmNsZSBjeD0iMTEiIGN5PSI4LjIiIHI9IjIuMSIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-julia: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDMyNSAzMDAiPgogIDxnIGNsYXNzPSJqcC1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjY2IzYzMzIj4KICAgIDxwYXRoIGQ9Ik0gMTUwLjg5ODQzOCAyMjUgQyAxNTAuODk4NDM4IDI2Ni40MjE4NzUgMTE3LjMyMDMxMiAzMDAgNzUuODk4NDM4IDMwMCBDIDM0LjQ3NjU2MiAzMDAgMC44OTg0MzggMjY2LjQyMTg3NSAwLjg5ODQzOCAyMjUgQyAwLjg5ODQzOCAxODMuNTc4MTI1IDM0LjQ3NjU2MiAxNTAgNzUuODk4NDM4IDE1MCBDIDExNy4zMjAzMTIgMTUwIDE1MC44OTg0MzggMTgzLjU3ODEyNSAxNTAuODk4NDM4IDIyNSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzM4OTgyNiI+CiAgICA8cGF0aCBkPSJNIDIzNy41IDc1IEMgMjM3LjUgMTE2LjQyMTg3NSAyMDMuOTIxODc1IDE1MCAxNjIuNSAxNTAgQyAxMjEuMDc4MTI1IDE1MCA4Ny41IDExNi40MjE4NzUgODcuNSA3NSBDIDg3LjUgMzMuNTc4MTI1IDEyMS4wNzgxMjUgMCAxNjIuNSAwIEMgMjAzLjkyMTg3NSAwIDIzNy41IDMzLjU3ODEyNSAyMzcuNSA3NSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzk1NThiMiI+CiAgICA8cGF0aCBkPSJNIDMyNC4xMDE1NjIgMjI1IEMgMzI0LjEwMTU2MiAyNjYuNDIxODc1IDI5MC41MjM0MzggMzAwIDI0OS4xMDE1NjIgMzAwIEMgMjA3LjY3OTY4OCAzMDAgMTc0LjEwMTU2MiAyNjYuNDIxODc1IDE3NC4xMDE1NjIgMjI1IEMgMTc0LjEwMTU2MiAxODMuNTc4MTI1IDIwNy42Nzk2ODggMTUwIDI0OS4xMDE1NjIgMTUwIEMgMjkwLjUyMzQzOCAxNTAgMzI0LjEwMTU2MiAxODMuNTc4MTI1IDMyNC4xMDE1NjIgMjI1Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-jupyter-favicon: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyIiBoZWlnaHQ9IjE2NSIgdmlld0JveD0iMCAwIDE1MiAxNjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgPGcgY2xhc3M9ImpwLWp1cHl0ZXItaWNvbi1jb2xvciIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA3ODk0NywgMTEwLjU4MjkyNykiIGQ9Ik03NS45NDIyODQyLDI5LjU4MDQ1NjEgQzQzLjMwMjM5NDcsMjkuNTgwNDU2MSAxNC43OTY3ODMyLDE3LjY1MzQ2MzQgMCwwIEM1LjUxMDgzMjExLDE1Ljg0MDY4MjkgMTUuNzgxNTM4OSwyOS41NjY3NzMyIDI5LjM5MDQ5NDcsMzkuMjc4NDE3MSBDNDIuOTk5Nyw0OC45ODk4NTM3IDU5LjI3MzcsNTQuMjA2NzgwNSA3NS45NjA1Nzg5LDU0LjIwNjc4MDUgQzkyLjY0NzQ1NzksNTQuMjA2NzgwNSAxMDguOTIxNDU4LDQ4Ljk4OTg1MzcgMTIyLjUzMDY2MywzOS4yNzg0MTcxIEMxMzYuMTM5NDUzLDI5LjU2Njc3MzIgMTQ2LjQxMDI4NCwxNS44NDA2ODI5IDE1MS45MjExNTgsMCBDMTM3LjA4Nzg2OCwxNy42NTM0NjM0IDEwOC41ODI1ODksMjkuNTgwNDU2MSA3NS45NDIyODQyLDI5LjU4MDQ1NjEgTDc1Ljk0MjI4NDIsMjkuNTgwNDU2MSBaIiAvPgogICAgPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMzczNjgsIDAuNzA0ODc4KSIgZD0iTTc1Ljk3ODQ1NzksMjQuNjI2NDA3MyBDMTA4LjYxODc2MywyNC42MjY0MDczIDEzNy4xMjQ0NTgsMzYuNTUzNDQxNSAxNTEuOTIxMTU4LDU0LjIwNjc4MDUgQzE0Ni40MTAyODQsMzguMzY2MjIyIDEzNi4xMzk0NTMsMjQuNjQwMTMxNyAxMjIuNTMwNjYzLDE0LjkyODQ4NzggQzEwOC45MjE0NTgsNS4yMTY4NDM5IDkyLjY0NzQ1NzksMCA3NS45NjA1Nzg5LDAgQzU5LjI3MzcsMCA0Mi45OTk3LDUuMjE2ODQzOSAyOS4zOTA0OTQ3LDE0LjkyODQ4NzggQzE1Ljc4MTUzODksMjQuNjQwMTMxNyA1LjUxMDgzMjExLDM4LjM2NjIyMiAwLDU0LjIwNjc4MDUgQzE0LjgzMzA4MTYsMzYuNTg5OTI5MyA0My4zMzg1Njg0LDI0LjYyNjQwNzMgNzUuOTc4NDU3OSwyNC42MjY0MDczIEw3NS45Nzg0NTc5LDI0LjYyNjQwNzMgWiIgLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-jupyter: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkiIGhlaWdodD0iNTEiIHZpZXdCb3g9IjAgMCAzOSA1MSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTYzOCAtMjI4MSkiPgogICAgIDxnIGNsYXNzPSJqcC1qdXB5dGVyLWljb24tY29sb3IiIGZpbGw9IiNGMzc3MjYiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5Ljc0IDIzMTEuOTgpIiBkPSJNIDE4LjI2NDYgNy4xMzQxMUMgMTAuNDE0NSA3LjEzNDExIDMuNTU4NzIgNC4yNTc2IDAgMEMgMS4zMjUzOSAzLjgyMDQgMy43OTU1NiA3LjEzMDgxIDcuMDY4NiA5LjQ3MzAzQyAxMC4zNDE3IDExLjgxNTIgMTQuMjU1NyAxMy4wNzM0IDE4LjI2OSAxMy4wNzM0QyAyMi4yODIzIDEzLjA3MzQgMjYuMTk2MyAxMS44MTUyIDI5LjQ2OTQgOS40NzMwM0MgMzIuNzQyNCA3LjEzMDgxIDM1LjIxMjYgMy44MjA0IDM2LjUzOCAwQyAzMi45NzA1IDQuMjU3NiAyNi4xMTQ4IDcuMTM0MTEgMTguMjY0NiA3LjEzNDExWiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5LjczIDIyODUuNDgpIiBkPSJNIDE4LjI3MzMgNS45MzkzMUMgMjYuMTIzNSA1LjkzOTMxIDMyLjk3OTMgOC44MTU4MyAzNi41MzggMTMuMDczNEMgMzUuMjEyNiA5LjI1MzAzIDMyLjc0MjQgNS45NDI2MiAyOS40Njk0IDMuNjAwNEMgMjYuMTk2MyAxLjI1ODE4IDIyLjI4MjMgMCAxOC4yNjkgMEMgMTQuMjU1NyAwIDEwLjM0MTcgMS4yNTgxOCA3LjA2ODYgMy42MDA0QyAzLjc5NTU2IDUuOTQyNjIgMS4zMjUzOSA5LjI1MzAzIDAgMTMuMDczNEMgMy41Njc0NSA4LjgyNDYzIDEwLjQyMzIgNS45MzkzMSAxOC4yNzMzIDUuOTM5MzFaIi8+CiAgICA8L2c+CiAgICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjY5LjMgMjI4MS4zMSkiIGQ9Ik0gNS44OTM1MyAyLjg0NEMgNS45MTg4OSAzLjQzMTY1IDUuNzcwODUgNC4wMTM2NyA1LjQ2ODE1IDQuNTE2NDVDIDUuMTY1NDUgNS4wMTkyMiA0LjcyMTY4IDUuNDIwMTUgNC4xOTI5OSA1LjY2ODUxQyAzLjY2NDMgNS45MTY4OCAzLjA3NDQ0IDYuMDAxNTEgMi40OTgwNSA1LjkxMTcxQyAxLjkyMTY2IDUuODIxOSAxLjM4NDYzIDUuNTYxNyAwLjk1NDg5OCA1LjE2NDAxQyAwLjUyNTE3IDQuNzY2MzMgMC4yMjIwNTYgNC4yNDkwMyAwLjA4MzkwMzcgMy42Nzc1N0MgLTAuMDU0MjQ4MyAzLjEwNjExIC0wLjAyMTIzIDIuNTA2MTcgMC4xNzg3ODEgMS45NTM2NEMgMC4zNzg3OTMgMS40MDExIDAuNzM2ODA5IDAuOTIwODE3IDEuMjA3NTQgMC41NzM1MzhDIDEuNjc4MjYgMC4yMjYyNTkgMi4yNDA1NSAwLjAyNzU5MTkgMi44MjMyNiAwLjAwMjY3MjI5QyAzLjYwMzg5IC0wLjAzMDcxMTUgNC4zNjU3MyAwLjI0OTc4OSA0Ljk0MTQyIDAuNzgyNTUxQyA1LjUxNzExIDEuMzE1MzEgNS44NTk1NiAyLjA1Njc2IDUuODkzNTMgMi44NDRaIi8+CiAgICAgIDxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE2MzkuOCAyMzIzLjgxKSIgZD0iTSA3LjQyNzg5IDMuNTgzMzhDIDcuNDYwMDggNC4zMjQzIDcuMjczNTUgNS4wNTgxOSA2Ljg5MTkzIDUuNjkyMTNDIDYuNTEwMzEgNi4zMjYwNyA1Ljk1MDc1IDYuODMxNTYgNS4yODQxMSA3LjE0NDZDIDQuNjE3NDcgNy40NTc2MyAzLjg3MzcxIDcuNTY0MTQgMy4xNDcwMiA3LjQ1MDYzQyAyLjQyMDMyIDcuMzM3MTIgMS43NDMzNiA3LjAwODcgMS4yMDE4NCA2LjUwNjk1QyAwLjY2MDMyOCA2LjAwNTIgMC4yNzg2MSA1LjM1MjY4IDAuMTA1MDE3IDQuNjMyMDJDIC0wLjA2ODU3NTcgMy45MTEzNSAtMC4wMjYyMzYxIDMuMTU0OTQgMC4yMjY2NzUgMi40NTg1NkMgMC40Nzk1ODcgMS43NjIxNyAwLjkzMTY5NyAxLjE1NzEzIDEuNTI1NzYgMC43MjAwMzNDIDIuMTE5ODMgMC4yODI5MzUgMi44MjkxNCAwLjAzMzQzOTUgMy41NjM4OSAwLjAwMzEzMzQ0QyA0LjU0NjY3IC0wLjAzNzQwMzMgNS41MDUyOSAwLjMxNjcwNiA2LjIyOTYxIDAuOTg3ODM1QyA2Ljk1MzkzIDEuNjU4OTYgNy4zODQ4NCAyLjU5MjM1IDcuNDI3ODkgMy41ODMzOEwgNy40Mjc4OSAzLjU4MzM4WiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM4LjM2IDIyODYuMDYpIiBkPSJNIDIuMjc0NzEgNC4zOTYyOUMgMS44NDM2MyA0LjQxNTA4IDEuNDE2NzEgNC4zMDQ0NSAxLjA0Nzk5IDQuMDc4NDNDIDAuNjc5MjY4IDMuODUyNCAwLjM4NTMyOCAzLjUyMTE0IDAuMjAzMzcxIDMuMTI2NTZDIDAuMDIxNDEzNiAyLjczMTk4IC0wLjA0MDM3OTggMi4yOTE4MyAwLjAyNTgxMTYgMS44NjE4MUMgMC4wOTIwMDMxIDEuNDMxOCAwLjI4MzIwNCAxLjAzMTI2IDAuNTc1MjEzIDAuNzEwODgzQyAwLjg2NzIyMiAwLjM5MDUxIDEuMjQ2OTEgMC4xNjQ3MDggMS42NjYyMiAwLjA2MjA1OTJDIDIuMDg1NTMgLTAuMDQwNTg5NyAyLjUyNTYxIC0wLjAxNTQ3MTQgMi45MzA3NiAwLjEzNDIzNUMgMy4zMzU5MSAwLjI4Mzk0MSAzLjY4NzkyIDAuNTUxNTA1IDMuOTQyMjIgMC45MDMwNkMgNC4xOTY1MiAxLjI1NDYyIDQuMzQxNjkgMS42NzQzNiA0LjM1OTM1IDIuMTA5MTZDIDQuMzgyOTkgMi42OTEwNyA0LjE3Njc4IDMuMjU4NjkgMy43ODU5NyAzLjY4NzQ2QyAzLjM5NTE2IDQuMTE2MjQgMi44NTE2NiA0LjM3MTE2IDIuMjc0NzEgNC4zOTYyOUwgMi4yNzQ3MSA0LjM5NjI5WiIvPgogICAgPC9nPgogIDwvZz4+Cjwvc3ZnPgo=);
  --jp-icon-jupyterlab-wordmark: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIHZpZXdCb3g9IjAgMCAxODYwLjggNDc1Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0RTRFNEUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ4MC4xMzY0MDEsIDY0LjI3MTQ5MykiPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsIDU4Ljg3NTU2NikiPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA4NzYwMywgMC4xNDAyOTQpIj4KICAgICAgICA8cGF0aCBkPSJNLTQyNi45LDE2OS44YzAsNDguNy0zLjcsNjQuNy0xMy42LDc2LjRjLTEwLjgsMTAtMjUsMTUuNS0zOS43LDE1LjVsMy43LDI5IGMyMi44LDAuMyw0NC44LTcuOSw2MS45LTIzLjFjMTcuOC0xOC41LDI0LTQ0LjEsMjQtODMuM1YwSC00Mjd2MTcwLjFMLTQyNi45LDE2OS44TC00MjYuOSwxNjkuOHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTU1LjA0NTI5NiwgNTYuODM3MTA0KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuNTYyNDUzLCAxLjc5OTg0MikiPgogICAgICAgIDxwYXRoIGQ9Ik0tMzEyLDE0OGMwLDIxLDAsMzkuNSwxLjcsNTUuNGgtMzEuOGwtMi4xLTMzLjNoLTAuOGMtNi43LDExLjYtMTYuNCwyMS4zLTI4LDI3LjkgYy0xMS42LDYuNi0yNC44LDEwLTM4LjIsOS44Yy0zMS40LDAtNjktMTcuNy02OS04OVYwaDM2LjR2MTEyLjdjMCwzOC43LDExLjYsNjQuNyw0NC42LDY0LjdjMTAuMy0wLjIsMjAuNC0zLjUsMjguOS05LjQgYzguNS01LjksMTUuMS0xNC4zLDE4LjktMjMuOWMyLjItNi4xLDMuMy0xMi41LDMuMy0xOC45VjAuMmgzNi40VjE0OEgtMzEyTC0zMTIsMTQ4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzOTAuMDEzMzIyLCA1My40Nzk2MzgpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS43MDY0NTgsIDAuMjMxNDI1KSI+CiAgICAgICAgPHBhdGggZD0iTS00NzguNiw3MS40YzAtMjYtMC44LTQ3LTEuNy02Ni43aDMyLjdsMS43LDM0LjhoMC44YzcuMS0xMi41LDE3LjUtMjIuOCwzMC4xLTI5LjcgYzEyLjUtNywyNi43LTEwLjMsNDEtOS44YzQ4LjMsMCw4NC43LDQxLjcsODQuNywxMDMuM2MwLDczLjEtNDMuNywxMDkuMi05MSwxMDkuMmMtMTIuMSwwLjUtMjQuMi0yLjItMzUtNy44IGMtMTAuOC01LjYtMTkuOS0xMy45LTI2LjYtMjQuMmgtMC44VjI5MWgtMzZ2LTIyMEwtNDc4LjYsNzEuNEwtNDc4LjYsNzEuNHogTS00NDIuNiwxMjUuNmMwLjEsNS4xLDAuNiwxMC4xLDEuNywxNS4xIGMzLDEyLjMsOS45LDIzLjMsMTkuOCwzMS4xYzkuOSw3LjgsMjIuMSwxMi4xLDM0LjcsMTIuMWMzOC41LDAsNjAuNy0zMS45LDYwLjctNzguNWMwLTQwLjctMjEuMS03NS42LTU5LjUtNzUuNiBjLTEyLjksMC40LTI1LjMsNS4xLTM1LjMsMTMuNGMtOS45LDguMy0xNi45LDE5LjctMTkuNiwzMi40Yy0xLjUsNC45LTIuMywxMC0yLjUsMTUuMVYxMjUuNkwtNDQyLjYsMTI1LjZMLTQ0Mi42LDEyNS42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDYuNzQwNzI2LCA1Ni44MzcxMDQpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC43NTEyMjYsIDEuOTg5Mjk5KSI+CiAgICAgICAgPHBhdGggZD0iTS00NDAuOCwwbDQzLjcsMTIwLjFjNC41LDEzLjQsOS41LDI5LjQsMTIuOCw0MS43aDAuOGMzLjctMTIuMiw3LjktMjcuNywxMi44LTQyLjQgbDM5LjctMTE5LjJoMzguNUwtMzQ2LjksMTQ1Yy0yNiw2OS43LTQzLjcsMTA1LjQtNjguNiwxMjcuMmMtMTIuNSwxMS43LTI3LjksMjAtNDQuNiwyMy45bC05LjEtMzEuMSBjMTEuNy0zLjksMjIuNS0xMC4xLDMxLjgtMTguMWMxMy4yLTExLjEsMjMuNy0yNS4yLDMwLjYtNDEuMmMxLjUtMi44LDIuNS01LjcsMi45LTguOGMtMC4zLTMuMy0xLjItNi42LTIuNS05LjdMLTQ4MC4yLDAuMSBoMzkuN0wtNDQwLjgsMEwtNDQwLjgsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoODIyLjc0ODEwNCwgMC4wMDAwMDApIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS40NjQwNTAsIDAuMzc4OTE0KSI+CiAgICAgICAgPHBhdGggZD0iTS00MTMuNywwdjU4LjNoNTJ2MjguMmgtNTJWMTk2YzAsMjUsNywzOS41LDI3LjMsMzkuNWM3LjEsMC4xLDE0LjItMC43LDIxLjEtMi41IGwxLjcsMjcuN2MtMTAuMywzLjctMjEuMyw1LjQtMzIuMiw1Yy03LjMsMC40LTE0LjYtMC43LTIxLjMtMy40Yy02LjgtMi43LTEyLjktNi44LTE3LjktMTIuMWMtMTAuMy0xMC45LTE0LjEtMjktMTQuMS01Mi45IFY4Ni41aC0zMVY1OC4zaDMxVjkuNkwtNDEzLjcsMEwtNDEzLjcsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOTc0LjQzMzI4NiwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuOTkwMDM0LCAwLjYxMDMzOSkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDQ1LjgsMTEzYzAuOCw1MCwzMi4yLDcwLjYsNjguNiw3MC42YzE5LDAuNiwzNy45LTMsNTUuMy0xMC41bDYuMiwyNi40IGMtMjAuOSw4LjktNDMuNSwxMy4xLTY2LjIsMTIuNmMtNjEuNSwwLTk4LjMtNDEuMi05OC4zLTEwMi41Qy00ODAuMiw0OC4yLTQ0NC43LDAtMzg2LjUsMGM2NS4yLDAsODIuNyw1OC4zLDgyLjcsOTUuNyBjLTAuMSw1LjgtMC41LDExLjUtMS4yLDE3LjJoLTE0MC42SC00NDUuOEwtNDQ1LjgsMTEzeiBNLTMzOS4yLDg2LjZjMC40LTIzLjUtOS41LTYwLjEtNTAuNC02MC4xIGMtMzYuOCwwLTUyLjgsMzQuNC01NS43LDYwLjFILTMzOS4yTC0zMzkuMiw4Ni42TC0zMzkuMiw4Ni42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjAxLjk2MTA1OCwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuMTc5NjQwLCAwLjcwNTA2OCkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDc4LjYsNjhjMC0yMy45LTAuNC00NC41LTEuNy02My40aDMxLjhsMS4yLDM5LjloMS43YzkuMS0yNy4zLDMxLTQ0LjUsNTUuMy00NC41IGMzLjUtMC4xLDcsMC40LDEwLjMsMS4ydjM0LjhjLTQuMS0wLjktOC4yLTEuMy0xMi40LTEuMmMtMjUuNiwwLTQzLjcsMTkuNy00OC43LDQ3LjRjLTEsNS43LTEuNiwxMS41LTEuNywxNy4ydjEwOC4zaC0zNlY2OCBMLTQ3OC42LDY4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCBkPSJNMTM1Mi4zLDMyNi4yaDM3VjI4aC0zN1YzMjYuMnogTTE2MDQuOCwzMjYuMmMtMi41LTEzLjktMy40LTMxLjEtMy40LTQ4Ljd2LTc2IGMwLTQwLjctMTUuMS04My4xLTc3LjMtODMuMWMtMjUuNiwwLTUwLDcuMS02Ni44LDE4LjFsOC40LDI0LjRjMTQuMy05LjIsMzQtMTUuMSw1My0xNS4xYzQxLjYsMCw0Ni4yLDMwLjIsNDYuMiw0N3Y0LjIgYy03OC42LTAuNC0xMjIuMywyNi41LTEyMi4zLDc1LjZjMCwyOS40LDIxLDU4LjQsNjIuMiw1OC40YzI5LDAsNTAuOS0xNC4zLDYyLjItMzAuMmgxLjNsMi45LDI1LjZIMTYwNC44eiBNMTU2NS43LDI1Ny43IGMwLDMuOC0wLjgsOC0yLjEsMTEuOGMtNS45LDE3LjItMjIuNywzNC00OS4yLDM0Yy0xOC45LDAtMzQuOS0xMS4zLTM0LjktMzUuM2MwLTM5LjUsNDUuOC00Ni42LDg2LjItNDUuOFYyNTcuN3ogTTE2OTguNSwzMjYuMiBsMS43LTMzLjZoMS4zYzE1LjEsMjYuOSwzOC43LDM4LjIsNjguMSwzOC4yYzQ1LjQsMCw5MS4yLTM2LjEsOTEuMi0xMDguOGMwLjQtNjEuNy0zNS4zLTEwMy43LTg1LjctMTAzLjcgYy0zMi44LDAtNTYuMywxNC43LTY5LjMsMzcuNGgtMC44VjI4aC0zNi42djI0NS43YzAsMTguMS0wLjgsMzguNi0xLjcsNTIuNUgxNjk4LjV6IE0xNzA0LjgsMjA4LjJjMC01LjksMS4zLTEwLjksMi4xLTE1LjEgYzcuNi0yOC4xLDMxLjEtNDUuNCw1Ni4zLTQ1LjRjMzkuNSwwLDYwLjUsMzQuOSw2MC41LDc1LjZjMCw0Ni42LTIzLjEsNzguMS02MS44LDc4LjFjLTI2LjksMC00OC4zLTE3LjYtNTUuNS00My4zIGMtMC44LTQuMi0xLjctOC44LTEuNy0xMy40VjIwOC4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzYxNjE2MSIgZD0iTTE1IDlIOXY2aDZWOXptLTIgNGgtMnYtMmgydjJ6bTgtMlY5aC0yVjdjMC0xLjEtLjktMi0yLTJoLTJWM2gtMnYyaC0yVjNIOXYySDdjLTEuMSAwLTIgLjktMiAydjJIM3YyaDJ2MkgzdjJoMnYyYzAgMS4xLjkgMiAyIDJoMnYyaDJ2LTJoMnYyaDJ2LTJoMmMxLjEgMCAyLS45IDItMnYtMmgydi0yaC0ydi0yaDJ6bS00IDZIN1Y3aDEwdjEweiIvPgo8L3N2Zz4K);
  --jp-icon-keyboard: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMTdjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY3YzAtMS4xLS45LTItMi0yem0tOSAzaDJ2MmgtMlY4em0wIDNoMnYyaC0ydi0yek04IDhoMnYySDhWOHptMCAzaDJ2Mkg4di0yem0tMSAySDV2LTJoMnYyem0wLTNINVY4aDJ2MnptOSA3SDh2LTJoOHYyem0wLTRoLTJ2LTJoMnYyem0wLTNoLTJWOGgydjJ6bTMgM2gtMnYtMmgydjJ6bTAtM2gtMlY4aDJ2MnoiLz4KPC9zdmc+Cg==);
  --jp-icon-launch: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMzIgMzIiIHdpZHRoPSIzMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yNiwyOEg2YTIuMDAyNywyLjAwMjcsMCwwLDEtMi0yVjZBMi4wMDI3LDIuMDAyNywwLDAsMSw2LDRIMTZWNkg2VjI2SDI2VjE2aDJWMjZBMi4wMDI3LDIuMDAyNywwLDAsMSwyNiwyOFoiLz4KICAgIDxwb2x5Z29uIHBvaW50cz0iMjAgMiAyMCA0IDI2LjU4NiA0IDE4IDEyLjU4NiAxOS40MTQgMTQgMjggNS40MTQgMjggMTIgMzAgMTIgMzAgMiAyMCAyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-launcher: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkgMTlINVY1aDdWM0g1YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMmgxNGMxLjEgMCAyLS45IDItMnYtN2gtMnY3ek0xNCAzdjJoMy41OWwtOS44MyA5LjgzIDEuNDEgMS40MUwxOSA2LjQxVjEwaDJWM2gtN3oiLz4KPC9zdmc+Cg==);
  --jp-icon-line-form: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGZpbGw9IndoaXRlIiBkPSJNNS44OCA0LjEyTDEzLjc2IDEybC03Ljg4IDcuODhMOCAyMmwxMC0xMEw4IDJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-link: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMuOSAxMmMwLTEuNzEgMS4zOS0zLjEgMy4xLTMuMWg0VjdIN2MtMi43NiAwLTUgMi4yNC01IDVzMi4yNCA1IDUgNWg0di0xLjlIN2MtMS43MSAwLTMuMS0xLjM5LTMuMS0zLjF6TTggMTNoOHYtMkg4djJ6bTktNmgtNHYxLjloNGMxLjcxIDAgMy4xIDEuMzkgMy4xIDMuMXMtMS4zOSAzLjEtMy4xIDMuMWgtNFYxN2g0YzIuNzYgMCA1LTIuMjQgNS01cy0yLjI0LTUtNS01eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xOSA1djE0SDVWNWgxNG0xLjEtMkgzLjljLS41IDAtLjkuNC0uOS45djE2LjJjMCAuNC40LjkuOS45aDE2LjJjLjQgMCAuOS0uNS45LS45VjMuOWMwLS41LS41LS45LS45LS45ek0xMSA3aDZ2MmgtNlY3em0wIDRoNnYyaC02di0yem0wIDRoNnYyaC02ek03IDdoMnYySDd6bTAgNGgydjJIN3ptMCA0aDJ2Mkg3eiIvPgo8L3N2Zz4K);
  --jp-icon-markdown: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjN0IxRkEyIiBkPSJNNSAxNC45aDEybC02LjEgNnptOS40LTYuOGMwLTEuMy0uMS0yLjktLjEtNC41LS40IDEuNC0uOSAyLjktMS4zIDQuM2wtMS4zIDQuM2gtMkw4LjUgNy45Yy0uNC0xLjMtLjctMi45LTEtNC4zLS4xIDEuNi0uMSAzLjItLjIgNC42TDcgMTIuNEg0LjhsLjctMTFoMy4zTDEwIDVjLjQgMS4yLjcgMi43IDEgMy45LjMtMS4yLjctMi42IDEtMy45bDEuMi0zLjdoMy4zbC42IDExaC0yLjRsLS4zLTQuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-move-down: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMTIuNDcxIDcuNTI4OTlDMTIuNzYzMiA3LjIzNjg0IDEyLjc2MzIgNi43NjMxNiAxMi40NzEgNi40NzEwMVY2LjQ3MTAxQzEyLjE3OSA2LjE3OTA1IDExLjcwNTcgNi4xNzg4NCAxMS40MTM1IDYuNDcwNTRMNy43NSAxMC4xMjc1VjEuNzVDNy43NSAxLjMzNTc5IDcuNDE0MjEgMSA3IDFWMUM2LjU4NTc5IDEgNi4yNSAxLjMzNTc5IDYuMjUgMS43NVYxMC4xMjc1TDIuNTk3MjYgNi40NjgyMkMyLjMwMzM4IDYuMTczODEgMS44MjY0MSA2LjE3MzU5IDEuNTMyMjYgNi40Njc3NFY2LjQ2Nzc0QzEuMjM4MyA2Ljc2MTcgMS4yMzgzIDcuMjM4MyAxLjUzMjI2IDcuNTMyMjZMNi4yOTI4OSAxMi4yOTI5QzYuNjgzNDIgMTIuNjgzNCA3LjMxNjU4IDEyLjY4MzQgNy43MDcxMSAxMi4yOTI5TDEyLjQ3MSA3LjUyODk5WiIgZmlsbD0iIzYxNjE2MSIvPgo8L3N2Zz4K);
  --jp-icon-move-up: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMS41Mjg5OSA2LjQ3MTAxQzEuMjM2ODQgNi43NjMxNiAxLjIzNjg0IDcuMjM2ODQgMS41Mjg5OSA3LjUyODk5VjcuNTI4OTlDMS44MjA5NSA3LjgyMDk1IDIuMjk0MjYgNy44MjExNiAyLjU4NjQ5IDcuNTI5NDZMNi4yNSAzLjg3MjVWMTIuMjVDNi4yNSAxMi42NjQyIDYuNTg1NzkgMTMgNyAxM1YxM0M3LjQxNDIxIDEzIDcuNzUgMTIuNjY0MiA3Ljc1IDEyLjI1VjMuODcyNUwxMS40MDI3IDcuNTMxNzhDMTEuNjk2NiA3LjgyNjE5IDEyLjE3MzYgNy44MjY0MSAxMi40Njc3IDcuNTMyMjZWNy41MzIyNkMxMi43NjE3IDcuMjM4MyAxMi43NjE3IDYuNzYxNyAxMi40Njc3IDYuNDY3NzRMNy43MDcxMSAxLjcwNzExQzcuMzE2NTggMS4zMTY1OCA2LjY4MzQyIDEuMzE2NTggNi4yOTI4OSAxLjcwNzExTDEuNTI4OTkgNi40NzEwMVoiIGZpbGw9IiM2MTYxNjEiLz4KPC9zdmc+Cg==);
  --jp-icon-new-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwIDZoLThsLTItMkg0Yy0xLjExIDAtMS45OS44OS0xLjk5IDJMMiAxOGMwIDEuMTEuODkgMiAyIDJoMTZjMS4xMSAwIDItLjg5IDItMlY4YzAtMS4xMS0uODktMi0yLTJ6bS0xIDhoLTN2M2gtMnYtM2gtM3YtMmgzVjloMnYzaDN2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-not-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI1IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMTkgMTcuMTg0NCAyLjk2OTY4IDE0LjMwMzIgMS44NjA5NCAxMS40NDA5WiIvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24yIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOS4zMTU5MiA5LjMyMDMxKSIgZD0iTTcuMzY4NDIgMEwwIDcuMzY0NzkiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDkuMzE1OTIgMTYuNjgzNikgc2NhbGUoMSAtMSkiIGQ9Ik03LjM2ODQyIDBMMCA3LjM2NDc5Ii8+Cjwvc3ZnPgo=);
  --jp-icon-notebook: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtbm90ZWJvb2staWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNFRjZDMDAiPgogICAgPHBhdGggZD0iTTE4LjcgMy4zdjE1LjRIMy4zVjMuM2gxNS40bTEuNS0xLjVIMS44djE4LjNoMTguM2wuMS0xOC4zeiIvPgogICAgPHBhdGggZD0iTTE2LjUgMTYuNWwtNS40LTQuMy01LjYgNC4zdi0xMWgxMXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-numbering: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTQgMTlINlYxOS41SDVWMjAuNUg2VjIxSDRWMjJIN1YxOEg0VjE5Wk01IDEwSDZWNkg0VjdINVYxMFpNNCAxM0g1LjhMNCAxNS4xVjE2SDdWMTVINS4yTDcgMTIuOVYxMkg0VjEzWk05IDdWOUgyM1Y3SDlaTTkgMjFIMjNWMTlIOVYyMVpNOSAxNUgyM1YxM0g5VjE1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-offline-bolt: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDIuMDJjLTUuNTEgMC05Ljk4IDQuNDctOS45OCA5Ljk4czQuNDcgOS45OCA5Ljk4IDkuOTggOS45OC00LjQ3IDkuOTgtOS45OFMxNy41MSAyLjAyIDEyIDIuMDJ6TTExLjQ4IDIwdi02LjI2SDhMMTMgNHY2LjI2aDMuMzVMMTEuNDggMjB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-palette: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE4IDEzVjIwSDRWNkg5LjAyQzkuMDcgNS4yOSA5LjI0IDQuNjIgOS41IDRINEMyLjkgNCAyIDQuOSAyIDZWMjBDMiAyMS4xIDIuOSAyMiA0IDIySDE4QzE5LjEgMjIgMjAgMjEuMSAyMCAyMFYxNUwxOCAxM1pNMTkuMyA4Ljg5QzE5Ljc0IDguMTkgMjAgNy4zOCAyMCA2LjVDMjAgNC4wMSAxNy45OSAyIDE1LjUgMkMxMy4wMSAyIDExIDQuMDEgMTEgNi41QzExIDguOTkgMTMuMDEgMTEgMTUuNDkgMTFDMTYuMzcgMTEgMTcuMTkgMTAuNzQgMTcuODggMTAuM0wyMSAxMy40MkwyMi40MiAxMkwxOS4zIDguODlaTTE1LjUgOUMxNC4xMiA5IDEzIDcuODggMTMgNi41QzEzIDUuMTIgMTQuMTIgNCAxNS41IDRDMTYuODggNCAxOCA1LjEyIDE4IDYuNUMxOCA3Ljg4IDE2Ljg4IDkgMTUuNSA5WiIvPgogICAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00IDZIOS4wMTg5NEM5LjAwNjM5IDYuMTY1MDIgOSA2LjMzMTc2IDkgNi41QzkgOC44MTU3NyAxMC4yMTEgMTAuODQ4NyAxMi4wMzQzIDEySDlWMTRIMTZWMTIuOTgxMUMxNi41NzAzIDEyLjkzNzcgMTcuMTIgMTIuODIwNyAxNy42Mzk2IDEyLjYzOTZMMTggMTNWMjBINFY2Wk04IDhINlYxMEg4VjhaTTYgMTJIOFYxNEg2VjEyWk04IDE2SDZWMThIOFYxNlpNOSAxNkgxNlYxOEg5VjE2WiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-paste: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE5IDJoLTQuMThDMTQuNC44NCAxMy4zIDAgMTIgMGMtMS4zIDAtMi40Ljg0LTIuODIgMkg1Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjRjMC0xLjEtLjktMi0yLTJ6bS03IDBjLjU1IDAgMSAuNDUgMSAxcy0uNDUgMS0xIDEtMS0uNDUtMS0xIC40NS0xIDEtMXptNyAxOEg1VjRoMnYzaDEwVjRoMnYxNnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-pdf: url(data:image/svg+xml;base64,PHN2ZwogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMiAyMiIgd2lkdGg9IjE2Ij4KICAgIDxwYXRoIHRyYW5zZm9ybT0icm90YXRlKDQ1KSIgY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0ZGMkEyQSIKICAgICAgIGQ9Im0gMjIuMzQ0MzY5LC0zLjAxNjM2NDIgaCA1LjYzODYwNCB2IDEuNTc5MjQzMyBoIC0zLjU0OTIyNyB2IDEuNTA4NjkyOTkgaCAzLjMzNzU3NiBWIDEuNjUwODE1NCBoIC0zLjMzNzU3NiB2IDMuNDM1MjYxMyBoIC0yLjA4OTM3NyB6IG0gLTcuMTM2NDQ0LDEuNTc5MjQzMyB2IDQuOTQzOTU0MyBoIDAuNzQ4OTIgcSAxLjI4MDc2MSwwIDEuOTUzNzAzLC0wLjYzNDk1MzUgMC42NzgzNjksLTAuNjM0OTUzNSAwLjY3ODM2OSwtMS44NDUxNjQxIDAsLTEuMjA0NzgzNTUgLTAuNjcyOTQyLC0xLjgzNDMxMDExIC0wLjY3Mjk0MiwtMC42Mjk1MjY1OSAtMS45NTkxMywtMC42Mjk1MjY1OSB6IG0gLTIuMDg5Mzc3LC0xLjU3OTI0MzMgaCAyLjIwMzM0MyBxIDEuODQ1MTY0LDAgMi43NDYwMzksMC4yNjU5MjA3IDAuOTA2MzAxLDAuMjYwNDkzNyAxLjU1MjEwOCwwLjg5MDAyMDMgMC41Njk4MywwLjU0ODEyMjMgMC44NDY2MDUsMS4yNjQ0ODAwNiAwLjI3Njc3NCwwLjcxNjM1NzgxIDAuMjc2Nzc0LDEuNjIyNjU4OTQgMCwwLjkxNzE1NTEgLTAuMjc2Nzc0LDEuNjM4OTM5OSAtMC4yNzY3NzUsMC43MTYzNTc4IC0wLjg0NjYwNSwxLjI2NDQ4IC0wLjY1MTIzNCwwLjYyOTUyNjYgLTEuNTYyOTYyLDAuODk1NDQ3MyAtMC45MTE3MjgsMC4yNjA0OTM3IC0yLjczNTE4NSwwLjI2MDQ5MzcgaCAtMi4yMDMzNDMgeiBtIC04LjE0NTg1NjUsMCBoIDMuNDY3ODIzIHEgMS41NDY2ODE2LDAgMi4zNzE1Nzg1LDAuNjg5MjIzIDAuODMwMzI0LDAuNjgzNzk2MSAwLjgzMDMyNCwxLjk1MzcwMzE0IDAsMS4yNzUzMzM5NyAtMC44MzAzMjQsMS45NjQ1NTcwNiBRIDkuOTg3MTk2MSwyLjI3NDkxNSA4LjQ0MDUxNDUsMi4yNzQ5MTUgSCA3LjA2MjA2ODQgViA1LjA4NjA3NjcgSCA0Ljk3MjY5MTUgWiBtIDIuMDg5Mzc2OSwxLjUxNDExOTkgdiAyLjI2MzAzOTQzIGggMS4xNTU5NDEgcSAwLjYwNzgxODgsMCAwLjkzODg2MjksLTAuMjkzMDU1NDcgMC4zMzEwNDQxLC0wLjI5ODQ4MjQxIDAuMzMxMDQ0MSwtMC44NDExNzc3MiAwLC0wLjU0MjY5NTMxIC0wLjMzMTA0NDEsLTAuODM1NzUwNzQgLTAuMzMxMDQ0MSwtMC4yOTMwNTU1IC0wLjkzODg2MjksLTAuMjkzMDU1NSB6IgovPgo8L3N2Zz4K);
  --jp-icon-python: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iLTEwIC0xMCAxMzEuMTYxMzYxNjk0MzM1OTQgMTMyLjM4ODk5OTkzODk2NDg0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzA2OTk4IiBkPSJNIDU0LjkxODc4NSw5LjE5Mjc0MjFlLTQgQyA1MC4zMzUxMzIsMC4wMjIyMTcyNyA0NS45NTc4NDYsMC40MTMxMzY5NyA0Mi4xMDYyODUsMS4wOTQ2NjkzIDMwLjc2MDA2OSwzLjA5OTE3MzEgMjguNzAwMDM2LDcuMjk0NzcxNCAyOC43MDAwMzUsMTUuMDMyMTY5IHYgMTAuMjE4NzUgaCAyNi44MTI1IHYgMy40MDYyNSBoIC0yNi44MTI1IC0xMC4wNjI1IGMgLTcuNzkyNDU5LDAgLTE0LjYxNTc1ODgsNC42ODM3MTcgLTE2Ljc0OTk5OTgsMTMuNTkzNzUgLTIuNDYxODE5OTgsMTAuMjEyOTY2IC0yLjU3MTAxNTA4LDE2LjU4NjAyMyAwLDI3LjI1IDEuOTA1OTI4Myw3LjkzNzg1MiA2LjQ1NzU0MzIsMTMuNTkzNzQ4IDE0LjI0OTk5OTgsMTMuNTkzNzUgaCA5LjIxODc1IHYgLTEyLjI1IGMgMCwtOC44NDk5MDIgNy42NTcxNDQsLTE2LjY1NjI0OCAxNi43NSwtMTYuNjU2MjUgaCAyNi43ODEyNSBjIDcuNDU0OTUxLDAgMTMuNDA2MjUzLC02LjEzODE2NCAxMy40MDYyNSwtMTMuNjI1IHYgLTI1LjUzMTI1IGMgMCwtNy4yNjYzMzg2IC02LjEyOTk4LC0xMi43MjQ3NzcxIC0xMy40MDYyNSwtMTMuOTM3NDk5NyBDIDY0LjI4MTU0OCwwLjMyNzk0Mzk3IDU5LjUwMjQzOCwtMC4wMjAzNzkwMyA1NC45MTg3ODUsOS4xOTI3NDIxZS00IFogbSAtMTQuNSw4LjIxODc1MDEyNTc5IGMgMi43Njk1NDcsMCA1LjAzMTI1LDIuMjk4NjQ1NiA1LjAzMTI1LDUuMTI0OTk5NiAtMmUtNiwyLjgxNjMzNiAtMi4yNjE3MDMsNS4wOTM3NSAtNS4wMzEyNSw1LjA5Mzc1IC0yLjc3OTQ3NiwtMWUtNiAtNS4wMzEyNSwtMi4yNzc0MTUgLTUuMDMxMjUsLTUuMDkzNzUgLTEwZS03LC0yLjgyNjM1MyAyLjI1MTc3NCwtNS4xMjQ5OTk2IDUuMDMxMjUsLTUuMTI0OTk5NiB6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2ZmZDQzYiIgZD0ibSA4NS42Mzc1MzUsMjguNjU3MTY5IHYgMTEuOTA2MjUgYyAwLDkuMjMwNzU1IC03LjgyNTg5NSwxNi45OTk5OTkgLTE2Ljc1LDE3IGggLTI2Ljc4MTI1IGMgLTcuMzM1ODMzLDAgLTEzLjQwNjI0OSw2LjI3ODQ4MyAtMTMuNDA2MjUsMTMuNjI1IHYgMjUuNTMxMjQ3IGMgMCw3LjI2NjM0NCA2LjMxODU4OCwxMS41NDAzMjQgMTMuNDA2MjUsMTMuNjI1MDA0IDguNDg3MzMxLDIuNDk1NjEgMTYuNjI2MjM3LDIuOTQ2NjMgMjYuNzgxMjUsMCA2Ljc1MDE1NSwtMS45NTQzOSAxMy40MDYyNTMsLTUuODg3NjEgMTMuNDA2MjUsLTEzLjYyNTAwNCBWIDg2LjUwMDkxOSBoIC0yNi43ODEyNSB2IC0zLjQwNjI1IGggMjYuNzgxMjUgMTMuNDA2MjU0IGMgNy43OTI0NjEsMCAxMC42OTYyNTEsLTUuNDM1NDA4IDEzLjQwNjI0MSwtMTMuNTkzNzUgMi43OTkzMywtOC4zOTg4ODYgMi42ODAyMiwtMTYuNDc1Nzc2IDAsLTI3LjI1IC0xLjkyNTc4LC03Ljc1NzQ0MSAtNS42MDM4NywtMTMuNTkzNzUgLTEzLjQwNjI0MSwtMTMuNTkzNzUgeiBtIC0xNS4wNjI1LDY0LjY1NjI1IGMgMi43Nzk0NzgsM2UtNiA1LjAzMTI1LDIuMjc3NDE3IDUuMDMxMjUsNS4wOTM3NDcgLTJlLTYsMi44MjYzNTQgLTIuMjUxNzc1LDUuMTI1MDA0IC01LjAzMTI1LDUuMTI1MDA0IC0yLjc2OTU1LDAgLTUuMDMxMjUsLTIuMjk4NjUgLTUuMDMxMjUsLTUuMTI1MDA0IDJlLTYsLTIuODE2MzMgMi4yNjE2OTcsLTUuMDkzNzQ3IDUuMDMxMjUsLTUuMDkzNzQ3IHoiLz4KPC9zdmc+Cg==);
  --jp-icon-r-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjE5NkYzIiBkPSJNNC40IDIuNWMxLjItLjEgMi45LS4zIDQuOS0uMyAyLjUgMCA0LjEuNCA1LjIgMS4zIDEgLjcgMS41IDEuOSAxLjUgMy41IDAgMi0xLjQgMy41LTIuOSA0LjEgMS4yLjQgMS43IDEuNiAyLjIgMyAuNiAxLjkgMSAzLjkgMS4zIDQuNmgtMy44Yy0uMy0uNC0uOC0xLjctMS4yLTMuN3MtMS4yLTIuNi0yLjYtMi42aC0uOXY2LjRINC40VjIuNXptMy43IDYuOWgxLjRjMS45IDAgMi45LS45IDIuOS0yLjNzLTEtMi4zLTIuOC0yLjNjLS43IDAtMS4zIDAtMS42LjJ2NC41aC4xdi0uMXoiLz4KPC9zdmc+Cg==);
  --jp-icon-react: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMTUwIDE1MCA1NDEuOSAyOTUuMyI+CiAgPGcgY2xhc3M9ImpwLWljb24tYnJhbmQyIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxREFGQiI+CiAgICA8cGF0aCBkPSJNNjY2LjMgMjk2LjVjMC0zMi41LTQwLjctNjMuMy0xMDMuMS04Mi40IDE0LjQtNjMuNiA4LTExNC4yLTIwLjItMTMwLjQtNi41LTMuOC0xNC4xLTUuNi0yMi40LTUuNnYyMi4zYzQuNiAwIDguMy45IDExLjQgMi42IDEzLjYgNy44IDE5LjUgMzcuNSAxNC45IDc1LjctMS4xIDkuNC0yLjkgMTkuMy01LjEgMjkuNC0xOS42LTQuOC00MS04LjUtNjMuNS0xMC45LTEzLjUtMTguNS0yNy41LTM1LjMtNDEuNi01MCAzMi42LTMwLjMgNjMuMi00Ni45IDg0LTQ2LjlWNzhjLTI3LjUgMC02My41IDE5LjYtOTkuOSA1My42LTM2LjQtMzMuOC03Mi40LTUzLjItOTkuOS01My4ydjIyLjNjMjAuNyAwIDUxLjQgMTYuNSA4NCA0Ni42LTE0IDE0LjctMjggMzEuNC00MS4zIDQ5LjktMjIuNiAyLjQtNDQgNi4xLTYzLjYgMTEtMi4zLTEwLTQtMTkuNy01LjItMjktNC43LTM4LjIgMS4xLTY3LjkgMTQuNi03NS44IDMtMS44IDYuOS0yLjYgMTEuNS0yLjZWNzguNWMtOC40IDAtMTYgMS44LTIyLjYgNS42LTI4LjEgMTYuMi0zNC40IDY2LjctMTkuOSAxMzAuMS02Mi4yIDE5LjItMTAyLjcgNDkuOS0xMDIuNyA4Mi4zIDAgMzIuNSA0MC43IDYzLjMgMTAzLjEgODIuNC0xNC40IDYzLjYtOCAxMTQuMiAyMC4yIDEzMC40IDYuNSAzLjggMTQuMSA1LjYgMjIuNSA1LjYgMjcuNSAwIDYzLjUtMTkuNiA5OS45LTUzLjYgMzYuNCAzMy44IDcyLjQgNTMuMiA5OS45IDUzLjIgOC40IDAgMTYtMS44IDIyLjYtNS42IDI4LjEtMTYuMiAzNC40LTY2LjcgMTkuOS0xMzAuMSA2Mi0xOS4xIDEwMi41LTQ5LjkgMTAyLjUtODIuM3ptLTEzMC4yLTY2LjdjLTMuNyAxMi45LTguMyAyNi4yLTEzLjUgMzkuNS00LjEtOC04LjQtMTYtMTMuMS0yNC00LjYtOC05LjUtMTUuOC0xNC40LTIzLjQgMTQuMiAyLjEgMjcuOSA0LjcgNDEgNy45em0tNDUuOCAxMDYuNWMtNy44IDEzLjUtMTUuOCAyNi4zLTI0LjEgMzguMi0xNC45IDEuMy0zMCAyLTQ1LjIgMi0xNS4xIDAtMzAuMi0uNy00NS0xLjktOC4zLTExLjktMTYuNC0yNC42LTI0LjItMzgtNy42LTEzLjEtMTQuNS0yNi40LTIwLjgtMzkuOCA2LjItMTMuNCAxMy4yLTI2LjggMjAuNy0zOS45IDcuOC0xMy41IDE1LjgtMjYuMyAyNC4xLTM4LjIgMTQuOS0xLjMgMzAtMiA0NS4yLTIgMTUuMSAwIDMwLjIuNyA0NSAxLjkgOC4zIDExLjkgMTYuNCAyNC42IDI0LjIgMzggNy42IDEzLjEgMTQuNSAyNi40IDIwLjggMzkuOC02LjMgMTMuNC0xMy4yIDI2LjgtMjAuNyAzOS45em0zMi4zLTEzYzUuNCAxMy40IDEwIDI2LjggMTMuOCAzOS44LTEzLjEgMy4yLTI2LjkgNS45LTQxLjIgOCA0LjktNy43IDkuOC0xNS42IDE0LjQtMjMuNyA0LjYtOCA4LjktMTYuMSAxMy0yNC4xek00MjEuMiA0MzBjLTkuMy05LjYtMTguNi0yMC4zLTI3LjgtMzIgOSAuNCAxOC4yLjcgMjcuNS43IDkuNCAwIDE4LjctLjIgMjcuOC0uNy05IDExLjctMTguMyAyMi40LTI3LjUgMzJ6bS03NC40LTU4LjljLTE0LjItMi4xLTI3LjktNC43LTQxLTcuOSAzLjctMTIuOSA4LjMtMjYuMiAxMy41LTM5LjUgNC4xIDggOC40IDE2IDEzLjEgMjQgNC43IDggOS41IDE1LjggMTQuNCAyMy40ek00MjAuNyAxNjNjOS4zIDkuNiAxOC42IDIwLjMgMjcuOCAzMi05LS40LTE4LjItLjctMjcuNS0uNy05LjQgMC0xOC43LjItMjcuOC43IDktMTEuNyAxOC4zLTIyLjQgMjcuNS0zMnptLTc0IDU4LjljLTQuOSA3LjctOS44IDE1LjYtMTQuNCAyMy43LTQuNiA4LTguOSAxNi0xMyAyNC01LjQtMTMuNC0xMC0yNi44LTEzLjgtMzkuOCAxMy4xLTMuMSAyNi45LTUuOCA0MS4yLTcuOXptLTkwLjUgMTI1LjJjLTM1LjQtMTUuMS01OC4zLTM0LjktNTguMy01MC42IDAtMTUuNyAyMi45LTM1LjYgNTguMy01MC42IDguNi0zLjcgMTgtNyAyNy43LTEwLjEgNS43IDE5LjYgMTMuMiA0MCAyMi41IDYwLjktOS4yIDIwLjgtMTYuNiA0MS4xLTIyLjIgNjAuNi05LjktMy4xLTE5LjMtNi41LTI4LTEwLjJ6TTMxMCA0OTBjLTEzLjYtNy44LTE5LjUtMzcuNS0xNC45LTc1LjcgMS4xLTkuNCAyLjktMTkuMyA1LjEtMjkuNCAxOS42IDQuOCA0MSA4LjUgNjMuNSAxMC45IDEzLjUgMTguNSAyNy41IDM1LjMgNDEuNiA1MC0zMi42IDMwLjMtNjMuMiA0Ni45LTg0IDQ2LjktNC41LS4xLTguMy0xLTExLjMtMi43em0yMzcuMi03Ni4yYzQuNyAzOC4yLTEuMSA2Ny45LTE0LjYgNzUuOC0zIDEuOC02LjkgMi42LTExLjUgMi42LTIwLjcgMC01MS40LTE2LjUtODQtNDYuNiAxNC0xNC43IDI4LTMxLjQgNDEuMy00OS45IDIyLjYtMi40IDQ0LTYuMSA2My42LTExIDIuMyAxMC4xIDQuMSAxOS44IDUuMiAyOS4xem0zOC41LTY2LjdjLTguNiAzLjctMTggNy0yNy43IDEwLjEtNS43LTE5LjYtMTMuMi00MC0yMi41LTYwLjkgOS4yLTIwLjggMTYuNi00MS4xIDIyLjItNjAuNiA5LjkgMy4xIDE5LjMgNi41IDI4LjEgMTAuMiAzNS40IDE1LjEgNTguMyAzNC45IDU4LjMgNTAuNi0uMSAxNS43LTIzIDM1LjYtNTguNCA1MC42ek0zMjAuOCA3OC40eiIvPgogICAgPGNpcmNsZSBjeD0iNDIwLjkiIGN5PSIyOTYuNSIgcj0iNDUuNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-redo: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIi8+PHBhdGggZD0iTTE4LjQgMTAuNkMxNi41NSA4Ljk5IDE0LjE1IDggMTEuNSA4Yy00LjY1IDAtOC41OCAzLjAzLTkuOTYgNy4yMkwzLjkgMTZjMS4wNS0zLjE5IDQuMDUtNS41IDcuNi01LjUgMS45NSAwIDMuNzMuNzIgNS4xMiAxLjg4TDEzIDE2aDlWN2wtMy42IDMuNnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-refresh: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTkgMTMuNWMtMi40OSAwLTQuNS0yLjAxLTQuNS00LjVTNi41MSA0LjUgOSA0LjVjMS4yNCAwIDIuMzYuNTIgMy4xNyAxLjMzTDEwIDhoNVYzbC0xLjc2IDEuNzZDMTIuMTUgMy42OCAxMC42NiAzIDkgMyA1LjY5IDMgMy4wMSA1LjY5IDMuMDEgOVM1LjY5IDE1IDkgMTVjMi45NyAwIDUuNDMtMi4xNiA1LjktNWgtMS41MmMtLjQ2IDItMi4yNCAzLjUtNC4zOCAzLjV6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-regex: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiBmaWxsPSIjRkZGIj4KICAgIDxjaXJjbGUgY2xhc3M9InN0MiIgY3g9IjUuNSIgY3k9IjE0LjUiIHI9IjEuNSIvPgogICAgPHJlY3QgeD0iMTIiIHk9IjQiIGNsYXNzPSJzdDIiIHdpZHRoPSIxIiBoZWlnaHQ9IjgiLz4KICAgIDxyZWN0IHg9IjguNSIgeT0iNy41IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjg2NiAtMC41IDAuNSAwLjg2NiAtMi4zMjU1IDcuMzIxOSkiIGNsYXNzPSJzdDIiIHdpZHRoPSI4IiBoZWlnaHQ9IjEiLz4KICAgIDxyZWN0IHg9IjEyIiB5PSI0IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjUgLTAuODY2IDAuODY2IDAuNSAtMC42Nzc5IDE0LjgyNTIpIiBjbGFzcz0ic3QyIiB3aWR0aD0iMSIgaGVpZ2h0PSI4Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-run: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTggNXYxNGwxMS03eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-running: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMjU2IDhDMTE5IDggOCAxMTkgOCAyNTZzMTExIDI0OCAyNDggMjQ4IDI0OC0xMTEgMjQ4LTI0OFMzOTMgOCAyNTYgOHptOTYgMzI4YzAgOC44LTcuMiAxNi0xNiAxNkgxNzZjLTguOCAwLTE2LTcuMi0xNi0xNlYxNzZjMC04LjggNy4yLTE2IDE2LTE2aDE2MGM4LjggMCAxNiA3LjIgMTYgMTZ2MTYweiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-save: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE3IDNINWMtMS4xMSAwLTIgLjktMiAydjE0YzAgMS4xLjg5IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjdsLTQtNHptLTUgMTZjLTEuNjYgMC0zLTEuMzQtMy0zczEuMzQtMyAzLTMgMyAxLjM0IDMgMy0xLjM0IDMtMyAzem0zLTEwSDVWNWgxMHY0eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-search: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjEsMTAuOWgtMC43bC0wLjItMC4yYzAuOC0wLjksMS4zLTIuMiwxLjMtMy41YzAtMy0yLjQtNS40LTUuNC01LjRTMS44LDQuMiwxLjgsNy4xczIuNCw1LjQsNS40LDUuNCBjMS4zLDAsMi41LTAuNSwzLjUtMS4zbDAuMiwwLjJ2MC43bDQuMSw0LjFsMS4yLTEuMkwxMi4xLDEwLjl6IE03LjEsMTAuOWMtMi4xLDAtMy43LTEuNy0zLjctMy43czEuNy0zLjcsMy43LTMuN3MzLjcsMS43LDMuNywzLjcgUzkuMiwxMC45LDcuMSwxMC45eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-settings: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuNDMgMTIuOThjLjA0LS4zMi4wNy0uNjQuMDctLjk4cy0uMDMtLjY2LS4wNy0uOThsMi4xMS0xLjY1Yy4xOS0uMTUuMjQtLjQyLjEyLS42NGwtMi0zLjQ2Yy0uMTItLjIyLS4zOS0uMy0uNjEtLjIybC0yLjQ5IDFjLS41Mi0uNC0xLjA4LS43My0xLjY5LS45OGwtLjM4LTIuNjVBLjQ4OC40ODggMCAwMDE0IDJoLTRjLS4yNSAwLS40Ni4xOC0uNDkuNDJsLS4zOCAyLjY1Yy0uNjEuMjUtMS4xNy41OS0xLjY5Ljk4bC0yLjQ5LTFjLS4yMy0uMDktLjQ5IDAtLjYxLjIybC0yIDMuNDZjLS4xMy4yMi0uMDcuNDkuMTIuNjRsMi4xMSAxLjY1Yy0uMDQuMzItLjA3LjY1LS4wNy45OHMuMDMuNjYuMDcuOThsLTIuMTEgMS42NWMtLjE5LjE1LS4yNC40Mi0uMTIuNjRsMiAzLjQ2Yy4xMi4yMi4zOS4zLjYxLjIybDIuNDktMWMuNTIuNCAxLjA4LjczIDEuNjkuOThsLjM4IDIuNjVjLjAzLjI0LjI0LjQyLjQ5LjQyaDRjLjI1IDAgLjQ2LS4xOC40OS0uNDJsLjM4LTIuNjVjLjYxLS4yNSAxLjE3LS41OSAxLjY5LS45OGwyLjQ5IDFjLjIzLjA5LjQ5IDAgLjYxLS4yMmwyLTMuNDZjLjEyLS4yMi4wNy0uNDktLjEyLS42NGwtMi4xMS0xLjY1ek0xMiAxNS41Yy0xLjkzIDAtMy41LTEuNTctMy41LTMuNXMxLjU3LTMuNSAzLjUtMy41IDMuNSAxLjU3IDMuNSAzLjUtMS41NyAzLjUtMy41IDMuNXoiLz4KPC9zdmc+Cg==);
  --jp-icon-share: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTSAxOCAyIEMgMTYuMzU0OTkgMiAxNSAzLjM1NDk5MDQgMTUgNSBDIDE1IDUuMTkwOTUyOSAxNS4wMjE3OTEgNS4zNzcxMjI0IDE1LjA1NjY0MSA1LjU1ODU5MzggTCA3LjkyMTg3NSA5LjcyMDcwMzEgQyA3LjM5ODUzOTkgOS4yNzc4NTM5IDYuNzMyMDc3MSA5IDYgOSBDIDQuMzU0OTkwNCA5IDMgMTAuMzU0OTkgMyAxMiBDIDMgMTMuNjQ1MDEgNC4zNTQ5OTA0IDE1IDYgMTUgQyA2LjczMjA3NzEgMTUgNy4zOTg1Mzk5IDE0LjcyMjE0NiA3LjkyMTg3NSAxNC4yNzkyOTcgTCAxNS4wNTY2NDEgMTguNDM5NDUzIEMgMTUuMDIxNTU1IDE4LjYyMTUxNCAxNSAxOC44MDgzODYgMTUgMTkgQyAxNSAyMC42NDUwMSAxNi4zNTQ5OSAyMiAxOCAyMiBDIDE5LjY0NTAxIDIyIDIxIDIwLjY0NTAxIDIxIDE5IEMgMjEgMTcuMzU0OTkgMTkuNjQ1MDEgMTYgMTggMTYgQyAxNy4yNjc0OCAxNiAxNi42MDE1OTMgMTYuMjc5MzI4IDE2LjA3ODEyNSAxNi43MjI2NTYgTCA4Ljk0MzM1OTQgMTIuNTU4NTk0IEMgOC45NzgyMDk1IDEyLjM3NzEyMiA5IDEyLjE5MDk1MyA5IDEyIEMgOSAxMS44MDkwNDcgOC45NzgyMDk1IDExLjYyMjg3OCA4Ljk0MzM1OTQgMTEuNDQxNDA2IEwgMTYuMDc4MTI1IDcuMjc5Mjk2OSBDIDE2LjYwMTQ2IDcuNzIyMTQ2MSAxNy4yNjc5MjMgOCAxOCA4IEMgMTkuNjQ1MDEgOCAyMSA2LjY0NTAwOTYgMjEgNSBDIDIxIDMuMzU0OTkwNCAxOS42NDUwMSAyIDE4IDIgeiBNIDE4IDQgQyAxOC41NjQxMjkgNCAxOSA0LjQzNTg3MDYgMTkgNSBDIDE5IDUuNTY0MTI5NCAxOC41NjQxMjkgNiAxOCA2IEMgMTcuNDM1ODcxIDYgMTcgNS41NjQxMjk0IDE3IDUgQyAxNyA0LjQzNTg3MDYgMTcuNDM1ODcxIDQgMTggNCB6IE0gNiAxMSBDIDYuNTY0MTI5NCAxMSA3IDExLjQzNTg3MSA3IDEyIEMgNyAxMi41NjQxMjkgNi41NjQxMjk0IDEzIDYgMTMgQyA1LjQzNTg3MDYgMTMgNSAxMi41NjQxMjkgNSAxMiBDIDUgMTEuNDM1ODcxIDUuNDM1ODcwNiAxMSA2IDExIHogTSAxOCAxOCBDIDE4LjU2NDEyOSAxOCAxOSAxOC40MzU4NzEgMTkgMTkgQyAxOSAxOS41NjQxMjkgMTguNTY0MTI5IDIwIDE4IDIwIEMgMTcuNDM1ODcxIDIwIDE3IDE5LjU2NDEyOSAxNyAxOSBDIDE3IDE4LjQzNTg3MSAxNy40MzU4NzEgMTggMTggMTggeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-spreadsheet: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNENBRjUwIiBkPSJNMi4yIDIuMnYxNy42aDE3LjZWMi4ySDIuMnptMTUuNCA3LjdoLTUuNVY0LjRoNS41djUuNXpNOS45IDQuNHY1LjVINC40VjQuNGg1LjV6bS01LjUgNy43aDUuNXY1LjVINC40di01LjV6bTcuNyA1LjV2LTUuNWg1LjV2NS41aC01LjV6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-stop: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik02IDZoMTJ2MTJINnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tab: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIxIDNIM2MtMS4xIDAtMiAuOS0yIDJ2MTRjMCAxLjEuOSAyIDIgMmgxOGMxLjEgMCAyLS45IDItMlY1YzAtMS4xLS45LTItMi0yem0wIDE2SDNWNWgxMHY0aDh2MTB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-table-rows: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMSw4SDNWNGgxOFY4eiBNMjEsMTBIM3Y0aDE4VjEweiBNMjEsMTZIM3Y0aDE4VjE2eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-tag: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjgiIHZpZXdCb3g9IjAgMCA0MyAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTI4LjgzMzIgMTIuMzM0TDMyLjk5OTggMTYuNTAwN0wzNy4xNjY1IDEyLjMzNEgyOC44MzMyWiIvPgoJCTxwYXRoIGQ9Ik0xNi4yMDk1IDIxLjYxMDRDMTUuNjg3MyAyMi4xMjk5IDE0Ljg0NDMgMjIuMTI5OSAxNC4zMjQ4IDIxLjYxMDRMNi45ODI5IDE0LjcyNDVDNi41NzI0IDE0LjMzOTQgNi4wODMxMyAxMy42MDk4IDYuMDQ3ODYgMTMuMDQ4MkM1Ljk1MzQ3IDExLjUyODggNi4wMjAwMiA4LjYxOTQ0IDYuMDY2MjEgNy4wNzY5NUM2LjA4MjgxIDYuNTE0NzcgNi41NTU0OCA2LjA0MzQ3IDcuMTE4MDQgNi4wMzA1NUM5LjA4ODYzIDUuOTg0NzMgMTMuMjYzOCA1LjkzNTc5IDEzLjY1MTggNi4zMjQyNUwyMS43MzY5IDEzLjYzOUMyMi4yNTYgMTQuMTU4NSAyMS43ODUxIDE1LjQ3MjQgMjEuMjYyIDE1Ljk5NDZMMTYuMjA5NSAyMS42MTA0Wk05Ljc3NTg1IDguMjY1QzkuMzM1NTEgNy44MjU2NiA4LjYyMzUxIDcuODI1NjYgOC4xODI4IDguMjY1QzcuNzQzNDYgOC43MDU3MSA3Ljc0MzQ2IDkuNDE3MzMgOC4xODI4IDkuODU2NjdDOC42MjM4MiAxMC4yOTY0IDkuMzM1ODIgMTAuMjk2NCA5Ljc3NTg1IDkuODU2NjdDMTAuMjE1NiA5LjQxNzMzIDEwLjIxNTYgOC43MDUzMyA5Ljc3NTg1IDguMjY1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-terminal: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiA+CiAgICA8cmVjdCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1iYWNrZ3JvdW5kLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgd2lkdGg9IjIwIiBoZWlnaHQ9IjIwIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyIDIpIiBmaWxsPSIjMzMzMzMzIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUtaW52ZXJzZSIgZD0iTTUuMDU2NjQgOC43NjE3MkM1LjA1NjY0IDguNTk3NjYgNS4wMzEyNSA4LjQ1MzEyIDQuOTgwNDcgOC4zMjgxMkM0LjkzMzU5IDguMTk5MjIgNC44NTU0NyA4LjA4MjAzIDQuNzQ2MDkgNy45NzY1NkM0LjY0MDYyIDcuODcxMDkgNC41IDcuNzc1MzkgNC4zMjQyMiA3LjY4OTQ1QzQuMTUyMzQgNy41OTk2MSAzLjk0MzM2IDcuNTExNzIgMy42OTcyNyA3LjQyNTc4QzMuMzAyNzMgNy4yODUxNiAyLjk0MzM2IDcuMTM2NzIgMi42MTkxNCA2Ljk4MDQ3QzIuMjk0OTIgNi44MjQyMiAyLjAxNzU4IDYuNjQyNTggMS43ODcxMSA2LjQzNTU1QzEuNTYwNTUgNi4yMjg1MiAxLjM4NDc3IDUuOTg4MjggMS4yNTk3NyA1LjcxNDg0QzEuMTM0NzcgNS40Mzc1IDEuMDcyMjcgNS4xMDkzOCAxLjA3MjI3IDQuNzMwNDdDMS4wNzIyNyA0LjM5ODQ0IDEuMTI4OTEgNC4wOTU3IDEuMjQyMTkgMy44MjIyN0MxLjM1NTQ3IDMuNTQ0OTIgMS41MTU2MiAzLjMwNDY5IDEuNzIyNjYgMy4xMDE1NkMxLjkyOTY5IDIuODk4NDQgMi4xNzk2OSAyLjczNDM3IDIuNDcyNjYgMi42MDkzOEMyLjc2NTYyIDIuNDg0MzggMy4wOTE4IDIuNDA0MyAzLjQ1MTE3IDIuMzY5MTRWMS4xMDkzOEg0LjM4ODY3VjIuMzgwODZDNC43NDAyMyAyLjQyNzczIDUuMDU2NjQgMi41MjM0NCA1LjMzNzg5IDIuNjY3OTdDNS42MTkxNCAyLjgxMjUgNS44NTc0MiAzLjAwMTk1IDYuMDUyNzMgMy4yMzYzM0M2LjI1MTk1IDMuNDY2OCA2LjQwNDMgMy43NDAyMyA2LjUwOTc3IDQuMDU2NjRDNi42MTkxNCA0LjM2OTE0IDYuNjczODMgNC43MjA3IDYuNjczODMgNS4xMTEzM0g1LjA0NDkyQzUuMDQ0OTIgNC42Mzg2NyA0LjkzNzUgNC4yODEyNSA0LjcyMjY2IDQuMDM5MDZDNC41MDc4MSAzLjc5Mjk3IDQuMjE2OCAzLjY2OTkyIDMuODQ5NjEgMy42Njk5MkMzLjY1MDM5IDMuNjY5OTIgMy40NzY1NiAzLjY5NzI3IDMuMzI4MTIgMy43NTE5NUMzLjE4MzU5IDMuODAyNzMgMy4wNjQ0NSAzLjg3Njk1IDIuOTcwNyAzLjk3NDYxQzIuODc2OTUgNC4wNjgzNiAyLjgwNjY0IDQuMTc5NjkgMi43NTk3NyA0LjMwODU5QzIuNzE2OCA0LjQzNzUgMi42OTUzMSA0LjU3ODEyIDIuNjk1MzEgNC43MzA0N0MyLjY5NTMxIDQuODgyODEgMi43MTY4IDUuMDE5NTMgMi43NTk3NyA1LjE0MDYyQzIuODA2NjQgNS4yNTc4MSAyLjg4MjgxIDUuMzY3MTkgMi45ODgyOCA1LjQ2ODc1QzMuMDk3NjYgNS41NzAzMSAzLjI0MDIzIDUuNjY3OTcgMy40MTYwMiA1Ljc2MTcyQzMuNTkxOCA1Ljg1MTU2IDMuODEwNTUgNS45NDMzNiA0LjA3MjI3IDYuMDM3MTFDNC40NjY4IDYuMTg1NTUgNC44MjQyMiA2LjMzOTg0IDUuMTQ0NTMgNi41QzUuNDY0ODQgNi42NTYyNSA1LjczODI4IDYuODM5ODQgNS45NjQ4NCA3LjA1MDc4QzYuMTk1MzEgNy4yNTc4MSA2LjM3MTA5IDcuNSA2LjQ5MjE5IDcuNzc3MzRDNi42MTcxOSA4LjA1MDc4IDYuNjc5NjkgOC4zNzUgNi42Nzk2OSA4Ljc1QzYuNjc5NjkgOS4wOTM3NSA2LjYyMzA1IDkuNDA0MyA2LjUwOTc3IDkuNjgxNjRDNi4zOTY0OCA5Ljk1NTA4IDYuMjM0MzggMTAuMTkxNCA2LjAyMzQ0IDEwLjM5MDZDNS44MTI1IDEwLjU4OTggNS41NTg1OSAxMC43NSA1LjI2MTcyIDEwLjg3MTFDNC45NjQ4NCAxMC45ODgzIDQuNjMyODEgMTEuMDY0NSA0LjI2NTYyIDExLjA5OTZWMTIuMjQ4SDMuMzMzOThWMTEuMDk5NkMzLjAwMTk1IDExLjA2ODQgMi42Nzk2OSAxMC45OTYxIDIuMzY3MTkgMTAuODgyOEMyLjA1NDY5IDEwLjc2NTYgMS43NzczNCAxMC41OTc3IDEuNTM1MTYgMTAuMzc4OUMxLjI5Njg4IDEwLjE2MDIgMS4xMDU0NyA5Ljg4NDc3IDAuOTYwOTM4IDkuNTUyNzNDMC44MTY0MDYgOS4yMTY4IDAuNzQ0MTQxIDguODE0NDUgMC43NDQxNDEgOC4zNDU3SDIuMzc4OTFDMi4zNzg5MSA4LjYyNjk1IDIuNDE5OTIgOC44NjMyOCAyLjUwMTk1IDkuMDU0NjlDMi41ODM5OCA5LjI0MjE5IDIuNjg5NDUgOS4zOTI1OCAyLjgxODM2IDkuNTA1ODZDMi45NTExNyA5LjYxNTIzIDMuMTAxNTYgOS42OTMzNiAzLjI2OTUzIDkuNzQwMjNDMy40Mzc1IDkuNzg3MTEgMy42MDkzOCA5LjgxMDU1IDMuNzg1MTYgOS44MTA1NUM0LjIwMzEyIDkuODEwNTUgNC41MTk1MyA5LjcxMjg5IDQuNzM0MzggOS41MTc1OEM0Ljk0OTIyIDkuMzIyMjcgNS4wNTY2NCA5LjA3MDMxIDUuMDU2NjQgOC43NjE3MlpNMTMuNDE4IDEyLjI3MTVIOC4wNzQyMlYxMUgxMy40MThWMTIuMjcxNVoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMuOTUyNjQgNikiIGZpbGw9IndoaXRlIi8+Cjwvc3ZnPgo=);
  --jp-icon-text-editor: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtdGV4dC1lZGl0b3ItaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xNSAxNUgzdjJoMTJ2LTJ6bTAtOEgzdjJoMTJWN3pNMyAxM2gxOHYtMkgzdjJ6bTAgOGgxOHYtMkgzdjJ6TTMgM3YyaDE4VjNIM3oiLz4KPC9zdmc+Cg==);
  --jp-icon-toc: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik03LDVIMjFWN0g3VjVNNywxM1YxMUgyMVYxM0g3TTQsNC41QTEuNSwxLjUgMCAwLDEgNS41LDZBMS41LDEuNSAwIDAsMSA0LDcuNUExLjUsMS41IDAgMCwxIDIuNSw2QTEuNSwxLjUgMCAwLDEgNCw0LjVNNCwxMC41QTEuNSwxLjUgMCAwLDEgNS41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMy41QTEuNSwxLjUgMCAwLDEgMi41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMC41TTcsMTlWMTdIMjFWMTlIN000LDE2LjVBMS41LDEuNSAwIDAsMSA1LjUsMThBMS41LDEuNSAwIDAsMSA0LDE5LjVBMS41LDEuNSAwIDAsMSAyLjUsMThBMS41LDEuNSAwIDAsMSA0LDE2LjVaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tree-view: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMiAxMVYzaC03djNIOVYzSDJ2OGg3VjhoMnYxMGg0djNoN3YtOGgtN3YzaC0yVjhoMnYzeiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMiAxNy4xODQ0IDIuOTY5NjggMTQuMzAzMiAxLjg2MDk0IDExLjQ0MDlaIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiMzMzMzMzMiIHN0cm9rZT0iIzMzMzMzMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOCA5Ljg2NzE5KSIgZD0iTTIuODYwMTUgNC44NjUzNUwwLjcyNjU0OSAyLjk5OTU5TDAgMy42MzA0NUwyLjg2MDE1IDYuMTMxNTdMOCAwLjYzMDg3Mkw3LjI3ODU3IDBMMi44NjAxNSA0Ljg2NTM1WiIvPgo8L3N2Zz4K);
  --jp-icon-undo: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjUgOGMtMi42NSAwLTUuMDUuOTktNi45IDIuNkwyIDd2OWg5bC0zLjYyLTMuNjJjMS4zOS0xLjE2IDMuMTYtMS44OCA1LjEyLTEuODggMy41NCAwIDYuNTUgMi4zMSA3LjYgNS41bDIuMzctLjc4QzIxLjA4IDExLjAzIDE3LjE1IDggMTIuNSA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-user: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE2IDdhNCA0IDAgMTEtOCAwIDQgNCAwIDAxOCAwek0xMiAxNGE3IDcgMCAwMC03IDdoMTRhNyA3IDAgMDAtNy03eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-users: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDM2IDI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogPGcgY2xhc3M9ImpwLWljb24zIiB0cmFuc2Zvcm09Im1hdHJpeCgxLjczMjcgMCAwIDEuNzMyNyAtMy42MjgyIC4wOTk1NzcpIiBmaWxsPSIjNjE2MTYxIj4KICA8cGF0aCB0cmFuc2Zvcm09Im1hdHJpeCgxLjUsMCwwLDEuNSwwLC02KSIgZD0ibTEyLjE4NiA3LjUwOThjLTEuMDUzNSAwLTEuOTc1NyAwLjU2NjUtMi40Nzg1IDEuNDEwMiAwLjc1MDYxIDAuMzEyNzcgMS4zOTc0IDAuODI2NDggMS44NzMgMS40NzI3aDMuNDg2M2MwLTEuNTkyLTEuMjg4OS0yLjg4MjgtMi44ODA5LTIuODgyOHoiLz4KICA8cGF0aCBkPSJtMjAuNDY1IDIuMzg5NWEyLjE4ODUgMi4xODg1IDAgMCAxLTIuMTg4NCAyLjE4ODUgMi4xODg1IDIuMTg4NSAwIDAgMS0yLjE4ODUtMi4xODg1IDIuMTg4NSAyLjE4ODUgMCAwIDEgMi4xODg1LTIuMTg4NSAyLjE4ODUgMi4xODg1IDAgMCAxIDIuMTg4NCAyLjE4ODV6Ii8+CiAgPHBhdGggdHJhbnNmb3JtPSJtYXRyaXgoMS41LDAsMCwxLjUsMCwtNikiIGQ9Im0zLjU4OTggOC40MjE5Yy0xLjExMjYgMC0yLjAxMzcgMC45MDExMS0yLjAxMzcgMi4wMTM3aDIuODE0NWMwLjI2Nzk3LTAuMzczMDkgMC41OTA3LTAuNzA0MzUgMC45NTg5OC0wLjk3ODUyLTAuMzQ0MzMtMC42MTY4OC0xLjAwMzEtMS4wMzUyLTEuNzU5OC0xLjAzNTJ6Ii8+CiAgPHBhdGggZD0ibTYuOTE1NCA0LjYyM2ExLjUyOTQgMS41Mjk0IDAgMCAxLTEuNTI5NCAxLjUyOTQgMS41Mjk0IDEuNTI5NCAwIDAgMS0xLjUyOTQtMS41Mjk0IDEuNTI5NCAxLjUyOTQgMCAwIDEgMS41Mjk0LTEuNTI5NCAxLjUyOTQgMS41Mjk0IDAgMCAxIDEuNTI5NCAxLjUyOTR6Ii8+CiAgPHBhdGggZD0ibTYuMTM1IDEzLjUzNWMwLTMuMjM5MiAyLjYyNTktNS44NjUgNS44NjUtNS44NjUgMy4yMzkyIDAgNS44NjUgMi42MjU5IDUuODY1IDUuODY1eiIvPgogIDxjaXJjbGUgY3g9IjEyIiBjeT0iMy43Njg1IiByPSIyLjk2ODUiLz4KIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-vega: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbjEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjEyMTIxIj4KICAgIDxwYXRoIGQ9Ik0xMC42IDUuNGwyLjItMy4ySDIuMnY3LjNsNC02LjZ6Ii8+CiAgICA8cGF0aCBkPSJNMTUuOCAyLjJsLTQuNCA2LjZMNyA2LjNsLTQuOCA4djUuNWgxNy42VjIuMmgtNHptLTcgMTUuNEg1LjV2LTQuNGgzLjN2NC40em00LjQgMEg5LjhWOS44aDMuNHY3Ljh6bTQuNCAwaC0zLjRWNi41aDMuNHYxMS4xeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-word: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KIDxnIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzQxNDE0MSI+CiAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiA8L2c+CiA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSguNDMgLjA0MDEpIiBmaWxsPSIjZmZmIj4KICA8cGF0aCBkPSJtNC4xNCA4Ljc2cTAuMDY4Mi0xLjg5IDIuNDItMS44OSAxLjE2IDAgMS42OCAwLjQyIDAuNTY3IDAuNDEgMC41NjcgMS4xNnYzLjQ3cTAgMC40NjIgMC41MTQgMC40NjIgMC4xMDMgMCAwLjItMC4wMjMxdjAuNzE0cS0wLjM5OSAwLjEwMy0wLjY1MSAwLjEwMy0wLjQ1MiAwLTAuNjkzLTAuMjItMC4yMzEtMC4yLTAuMjg0LTAuNjYyLTAuOTU2IDAuODcyLTIgMC44NzItMC45MDMgMC0xLjQ3LTAuNDcyLTAuNTI1LTAuNDcyLTAuNTI1LTEuMjYgMC0wLjI2MiAwLjA0NTItMC40NzIgMC4wNTY3LTAuMjIgMC4xMTYtMC4zNzggMC4wNjgyLTAuMTY4IDAuMjMxLTAuMzA0IDAuMTU4LTAuMTQ3IDAuMjYyLTAuMjQyIDAuMTE2LTAuMDkxNCAwLjM2OC0wLjE2OCAwLjI2Mi0wLjA5MTQgMC4zOTktMC4xMjYgMC4xMzYtMC4wNDUyIDAuNDcyLTAuMTAzIDAuMzM2LTAuMDU3OCAwLjUwNC0wLjA3OTggMC4xNTgtMC4wMjMxIDAuNTY3LTAuMDc5OCAwLjU1Ni0wLjA2ODIgMC43NzctMC4yMjEgMC4yMi0wLjE1MiAwLjIyLTAuNDQxdi0wLjI1MnEwLTAuNDMtMC4zNTctMC42NjItMC4zMzYtMC4yMzEtMC45NzYtMC4yMzEtMC42NjIgMC0wLjk5OCAwLjI2Mi0wLjMzNiAwLjI1Mi0wLjM5OSAwLjc5OHptMS44OSAzLjY4cTAuNzg4IDAgMS4yNi0wLjQxIDAuNTA0LTAuNDIgMC41MDQtMC45MDN2LTEuMDVxLTAuMjg0IDAuMTM2LTAuODYxIDAuMjMxLTAuNTY3IDAuMDkxNC0wLjk4NyAwLjE1OC0wLjQyIDAuMDY4Mi0wLjc2NiAwLjMyNi0wLjMzNiAwLjI1Mi0wLjMzNiAwLjcwNHQwLjMwNCAwLjcwNCAwLjg2MSAwLjI1MnoiIHN0cm9rZS13aWR0aD0iMS4wNSIvPgogIDxwYXRoIGQ9Im0xMCA0LjU2aDAuOTQ1djMuMTVxMC42NTEtMC45NzYgMS44OS0wLjk3NiAxLjE2IDAgMS44OSAwLjg0IDAuNjgyIDAuODQgMC42ODIgMi4zMSAwIDEuNDctMC43MDQgMi40Mi0wLjcwNCAwLjg4Mi0xLjg5IDAuODgyLTEuMjYgMC0xLjg5LTEuMDJ2MC43NjZoLTAuODV6bTIuNjIgMy4wNHEtMC43NDYgMC0xLjE2IDAuNjQtMC40NTIgMC42My0wLjQ1MiAxLjY4IDAgMS4wNSAwLjQ1MiAxLjY4dDEuMTYgMC42M3EwLjc3NyAwIDEuMjYtMC42MyAwLjQ5NC0wLjY0IDAuNDk0LTEuNjggMC0xLjA1LTAuNDcyLTEuNjgtMC40NjItMC42NC0xLjI2LTAuNjR6IiBzdHJva2Utd2lkdGg9IjEuMDUiLz4KICA8cGF0aCBkPSJtMi43MyAxNS44IDEzLjYgMC4wMDgxYzAuMDA2OSAwIDAtMi42IDAtMi42IDAtMC4wMDc4LTEuMTUgMC0xLjE1IDAtMC4wMDY5IDAtMC4wMDgzIDEuNS0wLjAwODMgMS41LTJlLTMgLTAuMDAxNC0xMS4zLTAuMDAxNC0xMS4zLTAuMDAxNGwtMC4wMDU5Mi0xLjVjMC0wLjAwNzgtMS4xNyAwLjAwMTMtMS4xNyAwLjAwMTN6IiBzdHJva2Utd2lkdGg9Ii45NzUiLz4KIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-yaml: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1jb250cmFzdDIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjRDgxQjYwIj4KICAgIDxwYXRoIGQ9Ik03LjIgMTguNnYtNS40TDMgNS42aDMuM2wxLjQgMy4xYy4zLjkuNiAxLjYgMSAyLjUuMy0uOC42LTEuNiAxLTIuNWwxLjQtMy4xaDMuNGwtNC40IDcuNnY1LjVsLTIuOS0uMXoiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxNi41IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxMSIgcj0iMi4xIi8+CiAgPC9nPgo8L3N2Zz4K);
}

/* Icon CSS class declarations */

.jp-AddAboveIcon {
  background-image: var(--jp-icon-add-above);
}

.jp-AddBelowIcon {
  background-image: var(--jp-icon-add-below);
}

.jp-AddIcon {
  background-image: var(--jp-icon-add);
}

.jp-BellIcon {
  background-image: var(--jp-icon-bell);
}

.jp-BugDotIcon {
  background-image: var(--jp-icon-bug-dot);
}

.jp-BugIcon {
  background-image: var(--jp-icon-bug);
}

.jp-BuildIcon {
  background-image: var(--jp-icon-build);
}

.jp-CaretDownEmptyIcon {
  background-image: var(--jp-icon-caret-down-empty);
}

.jp-CaretDownEmptyThinIcon {
  background-image: var(--jp-icon-caret-down-empty-thin);
}

.jp-CaretDownIcon {
  background-image: var(--jp-icon-caret-down);
}

.jp-CaretLeftIcon {
  background-image: var(--jp-icon-caret-left);
}

.jp-CaretRightIcon {
  background-image: var(--jp-icon-caret-right);
}

.jp-CaretUpEmptyThinIcon {
  background-image: var(--jp-icon-caret-up-empty-thin);
}

.jp-CaretUpIcon {
  background-image: var(--jp-icon-caret-up);
}

.jp-CaseSensitiveIcon {
  background-image: var(--jp-icon-case-sensitive);
}

.jp-CheckIcon {
  background-image: var(--jp-icon-check);
}

.jp-CircleEmptyIcon {
  background-image: var(--jp-icon-circle-empty);
}

.jp-CircleIcon {
  background-image: var(--jp-icon-circle);
}

.jp-ClearIcon {
  background-image: var(--jp-icon-clear);
}

.jp-CloseIcon {
  background-image: var(--jp-icon-close);
}

.jp-CodeCheckIcon {
  background-image: var(--jp-icon-code-check);
}

.jp-CodeIcon {
  background-image: var(--jp-icon-code);
}

.jp-CollapseAllIcon {
  background-image: var(--jp-icon-collapse-all);
}

.jp-ConsoleIcon {
  background-image: var(--jp-icon-console);
}

.jp-CopyIcon {
  background-image: var(--jp-icon-copy);
}

.jp-CopyrightIcon {
  background-image: var(--jp-icon-copyright);
}

.jp-CutIcon {
  background-image: var(--jp-icon-cut);
}

.jp-DeleteIcon {
  background-image: var(--jp-icon-delete);
}

.jp-DownloadIcon {
  background-image: var(--jp-icon-download);
}

.jp-DuplicateIcon {
  background-image: var(--jp-icon-duplicate);
}

.jp-EditIcon {
  background-image: var(--jp-icon-edit);
}

.jp-EllipsesIcon {
  background-image: var(--jp-icon-ellipses);
}

.jp-ErrorIcon {
  background-image: var(--jp-icon-error);
}

.jp-ExpandAllIcon {
  background-image: var(--jp-icon-expand-all);
}

.jp-ExtensionIcon {
  background-image: var(--jp-icon-extension);
}

.jp-FastForwardIcon {
  background-image: var(--jp-icon-fast-forward);
}

.jp-FileIcon {
  background-image: var(--jp-icon-file);
}

.jp-FileUploadIcon {
  background-image: var(--jp-icon-file-upload);
}

.jp-FilterDotIcon {
  background-image: var(--jp-icon-filter-dot);
}

.jp-FilterIcon {
  background-image: var(--jp-icon-filter);
}

.jp-FilterListIcon {
  background-image: var(--jp-icon-filter-list);
}

.jp-FolderFavoriteIcon {
  background-image: var(--jp-icon-folder-favorite);
}

.jp-FolderIcon {
  background-image: var(--jp-icon-folder);
}

.jp-HomeIcon {
  background-image: var(--jp-icon-home);
}

.jp-Html5Icon {
  background-image: var(--jp-icon-html5);
}

.jp-ImageIcon {
  background-image: var(--jp-icon-image);
}

.jp-InfoIcon {
  background-image: var(--jp-icon-info);
}

.jp-InspectorIcon {
  background-image: var(--jp-icon-inspector);
}

.jp-JsonIcon {
  background-image: var(--jp-icon-json);
}

.jp-JuliaIcon {
  background-image: var(--jp-icon-julia);
}

.jp-JupyterFaviconIcon {
  background-image: var(--jp-icon-jupyter-favicon);
}

.jp-JupyterIcon {
  background-image: var(--jp-icon-jupyter);
}

.jp-JupyterlabWordmarkIcon {
  background-image: var(--jp-icon-jupyterlab-wordmark);
}

.jp-KernelIcon {
  background-image: var(--jp-icon-kernel);
}

.jp-KeyboardIcon {
  background-image: var(--jp-icon-keyboard);
}

.jp-LaunchIcon {
  background-image: var(--jp-icon-launch);
}

.jp-LauncherIcon {
  background-image: var(--jp-icon-launcher);
}

.jp-LineFormIcon {
  background-image: var(--jp-icon-line-form);
}

.jp-LinkIcon {
  background-image: var(--jp-icon-link);
}

.jp-ListIcon {
  background-image: var(--jp-icon-list);
}

.jp-MarkdownIcon {
  background-image: var(--jp-icon-markdown);
}

.jp-MoveDownIcon {
  background-image: var(--jp-icon-move-down);
}

.jp-MoveUpIcon {
  background-image: var(--jp-icon-move-up);
}

.jp-NewFolderIcon {
  background-image: var(--jp-icon-new-folder);
}

.jp-NotTrustedIcon {
  background-image: var(--jp-icon-not-trusted);
}

.jp-NotebookIcon {
  background-image: var(--jp-icon-notebook);
}

.jp-NumberingIcon {
  background-image: var(--jp-icon-numbering);
}

.jp-OfflineBoltIcon {
  background-image: var(--jp-icon-offline-bolt);
}

.jp-PaletteIcon {
  background-image: var(--jp-icon-palette);
}

.jp-PasteIcon {
  background-image: var(--jp-icon-paste);
}

.jp-PdfIcon {
  background-image: var(--jp-icon-pdf);
}

.jp-PythonIcon {
  background-image: var(--jp-icon-python);
}

.jp-RKernelIcon {
  background-image: var(--jp-icon-r-kernel);
}

.jp-ReactIcon {
  background-image: var(--jp-icon-react);
}

.jp-RedoIcon {
  background-image: var(--jp-icon-redo);
}

.jp-RefreshIcon {
  background-image: var(--jp-icon-refresh);
}

.jp-RegexIcon {
  background-image: var(--jp-icon-regex);
}

.jp-RunIcon {
  background-image: var(--jp-icon-run);
}

.jp-RunningIcon {
  background-image: var(--jp-icon-running);
}

.jp-SaveIcon {
  background-image: var(--jp-icon-save);
}

.jp-SearchIcon {
  background-image: var(--jp-icon-search);
}

.jp-SettingsIcon {
  background-image: var(--jp-icon-settings);
}

.jp-ShareIcon {
  background-image: var(--jp-icon-share);
}

.jp-SpreadsheetIcon {
  background-image: var(--jp-icon-spreadsheet);
}

.jp-StopIcon {
  background-image: var(--jp-icon-stop);
}

.jp-TabIcon {
  background-image: var(--jp-icon-tab);
}

.jp-TableRowsIcon {
  background-image: var(--jp-icon-table-rows);
}

.jp-TagIcon {
  background-image: var(--jp-icon-tag);
}

.jp-TerminalIcon {
  background-image: var(--jp-icon-terminal);
}

.jp-TextEditorIcon {
  background-image: var(--jp-icon-text-editor);
}

.jp-TocIcon {
  background-image: var(--jp-icon-toc);
}

.jp-TreeViewIcon {
  background-image: var(--jp-icon-tree-view);
}

.jp-TrustedIcon {
  background-image: var(--jp-icon-trusted);
}

.jp-UndoIcon {
  background-image: var(--jp-icon-undo);
}

.jp-UserIcon {
  background-image: var(--jp-icon-user);
}

.jp-UsersIcon {
  background-image: var(--jp-icon-users);
}

.jp-VegaIcon {
  background-image: var(--jp-icon-vega);
}

.jp-WordIcon {
  background-image: var(--jp-icon-word);
}

.jp-YamlIcon {
  background-image: var(--jp-icon-yaml);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

.jp-Icon,
.jp-MaterialIcon {
  background-position: center;
  background-repeat: no-repeat;
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-cover {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

/**
 * (DEPRECATED) Support for specific CSS icon sizes
 */

.jp-Icon-16 {
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-18 {
  background-size: 18px;
  min-width: 18px;
  min-height: 18px;
}

.jp-Icon-20 {
  background-size: 20px;
  min-width: 20px;
  min-height: 20px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.lm-TabBar .lm-TabBar-addButton {
  align-items: center;
  display: flex;
  padding: 4px;
  padding-bottom: 5px;
  margin-right: 1px;
  background-color: var(--jp-layout-color2);
}

.lm-TabBar .lm-TabBar-addButton:hover {
  background-color: var(--jp-layout-color1);
}

.lm-DockPanel-tabBar .lm-TabBar-tab {
  width: var(--jp-private-horizontal-tab-width);
}

.lm-DockPanel-tabBar .lm-TabBar-content {
  flex: unset;
}

.lm-DockPanel-tabBar[data-orientation='horizontal'] {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for icons as inline SVG HTMLElements
 */

/* recolor the primary elements of an icon */
.jp-icon0[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon1[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon2[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon3[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-accent0[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-accent1[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-accent2[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-accent3[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-accent4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-accent0[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-accent1[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-accent2[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-accent3[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-accent4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-none[fill] {
  fill: none;
}

.jp-icon-none[stroke] {
  stroke: none;
}

/* brand icon colors. Same for light and dark */
.jp-icon-brand0[fill] {
  fill: var(--jp-brand-color0);
}

.jp-icon-brand1[fill] {
  fill: var(--jp-brand-color1);
}

.jp-icon-brand2[fill] {
  fill: var(--jp-brand-color2);
}

.jp-icon-brand3[fill] {
  fill: var(--jp-brand-color3);
}

.jp-icon-brand4[fill] {
  fill: var(--jp-brand-color4);
}

.jp-icon-brand0[stroke] {
  stroke: var(--jp-brand-color0);
}

.jp-icon-brand1[stroke] {
  stroke: var(--jp-brand-color1);
}

.jp-icon-brand2[stroke] {
  stroke: var(--jp-brand-color2);
}

.jp-icon-brand3[stroke] {
  stroke: var(--jp-brand-color3);
}

.jp-icon-brand4[stroke] {
  stroke: var(--jp-brand-color4);
}

/* warn icon colors. Same for light and dark */
.jp-icon-warn0[fill] {
  fill: var(--jp-warn-color0);
}

.jp-icon-warn1[fill] {
  fill: var(--jp-warn-color1);
}

.jp-icon-warn2[fill] {
  fill: var(--jp-warn-color2);
}

.jp-icon-warn3[fill] {
  fill: var(--jp-warn-color3);
}

.jp-icon-warn0[stroke] {
  stroke: var(--jp-warn-color0);
}

.jp-icon-warn1[stroke] {
  stroke: var(--jp-warn-color1);
}

.jp-icon-warn2[stroke] {
  stroke: var(--jp-warn-color2);
}

.jp-icon-warn3[stroke] {
  stroke: var(--jp-warn-color3);
}

/* icon colors that contrast well with each other and most backgrounds */
.jp-icon-contrast0[fill] {
  fill: var(--jp-icon-contrast-color0);
}

.jp-icon-contrast1[fill] {
  fill: var(--jp-icon-contrast-color1);
}

.jp-icon-contrast2[fill] {
  fill: var(--jp-icon-contrast-color2);
}

.jp-icon-contrast3[fill] {
  fill: var(--jp-icon-contrast-color3);
}

.jp-icon-contrast0[stroke] {
  stroke: var(--jp-icon-contrast-color0);
}

.jp-icon-contrast1[stroke] {
  stroke: var(--jp-icon-contrast-color1);
}

.jp-icon-contrast2[stroke] {
  stroke: var(--jp-icon-contrast-color2);
}

.jp-icon-contrast3[stroke] {
  stroke: var(--jp-icon-contrast-color3);
}

.jp-icon-dot[fill] {
  fill: var(--jp-warn-color0);
}

.jp-jupyter-icon-color[fill] {
  fill: var(--jp-jupyter-icon-color, var(--jp-warn-color0));
}

.jp-notebook-icon-color[fill] {
  fill: var(--jp-notebook-icon-color, var(--jp-warn-color0));
}

.jp-json-icon-color[fill] {
  fill: var(--jp-json-icon-color, var(--jp-warn-color1));
}

.jp-console-icon-color[fill] {
  fill: var(--jp-console-icon-color, white);
}

.jp-console-icon-background-color[fill] {
  fill: var(--jp-console-icon-background-color, var(--jp-brand-color1));
}

.jp-terminal-icon-color[fill] {
  fill: var(--jp-terminal-icon-color, var(--jp-layout-color2));
}

.jp-terminal-icon-background-color[fill] {
  fill: var(
    --jp-terminal-icon-background-color,
    var(--jp-inverse-layout-color2)
  );
}

.jp-text-editor-icon-color[fill] {
  fill: var(--jp-text-editor-icon-color, var(--jp-inverse-layout-color3));
}

.jp-inspector-icon-color[fill] {
  fill: var(--jp-inspector-icon-color, var(--jp-inverse-layout-color3));
}

/* CSS for icons in selected filebrowser listing items */
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

.jp-DirListing-item.jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* stylelint-disable selector-max-class, selector-max-compound-selectors */

/**
* TODO: come up with non css-hack solution for showing the busy icon on top
*  of the close icon
* CSS for complex behavior of close icon of tabs in the main area tabbar
*/
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}

.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

/* stylelint-enable selector-max-class, selector-max-compound-selectors */

/* CSS for icons in status bar */
#jp-main-statusbar .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

#jp-main-statusbar .jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* special handling for splash icon CSS. While the theme CSS reloads during
   splash, the splash icon can loose theming. To prevent that, we set a
   default for its color variable */
:root {
  --jp-warn-color0: var(--md-orange-700);
}

/* not sure what to do with this one, used in filebrowser listing */
.jp-DragIcon {
  margin-right: 4px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for alt colors for icons as inline SVG HTMLElements
 */

/* alt recolor the primary elements of an icon */
.jp-icon-alt .jp-icon0[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-alt .jp-icon1[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-alt .jp-icon2[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-alt .jp-icon3[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-alt .jp-icon4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-alt .jp-icon0[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-alt .jp-icon1[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-alt .jp-icon2[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-alt .jp-icon3[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-alt .jp-icon4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* alt recolor the accent elements of an icon */
.jp-icon-alt .jp-icon-accent0[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-alt .jp-icon-accent1[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-alt .jp-icon-accent2[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-alt .jp-icon-accent3[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-alt .jp-icon-accent4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-alt .jp-icon-accent0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-alt .jp-icon-accent1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-alt .jp-icon-accent2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-alt .jp-icon-accent3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-alt .jp-icon-accent4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-icon-hoverShow:not(:hover) .jp-icon-hoverShow-content {
  display: none !important;
}

/**
 * Support for hover colors for icons as inline SVG HTMLElements
 */

/**
 * regular colors
 */

/* recolor the primary elements of an icon */
.jp-icon-hover :hover .jp-icon0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-hover :hover .jp-icon1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-hover :hover .jp-icon2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-hover :hover .jp-icon3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-hover :hover .jp-icon4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-hover :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-hover :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-hover :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-hover :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-hover :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-hover :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-hover :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-hover :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-hover :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-hover :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-hover :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-hover :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-hover :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-hover :hover .jp-icon-none-hover[fill] {
  fill: none;
}

.jp-icon-hover :hover .jp-icon-none-hover[stroke] {
  stroke: none;
}

/**
 * inverse colors
 */

/* inverse recolor the primary elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* inverse recolor the accent elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-IFrame {
  width: 100%;
  height: 100%;
}

.jp-IFrame > iframe {
  border: none;
}

/*
When drag events occur, `lm-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-IFrame {
  position: relative;
}

body.lm-mod-override-cursor .jp-IFrame::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-HoverBox {
  position: fixed;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FormGroup-content fieldset {
  border: none;
  padding: 0;
  min-width: 0;
  width: 100%;
}

/* stylelint-disable selector-max-type */

.jp-FormGroup-content fieldset .jp-inputFieldWrapper input,
.jp-FormGroup-content fieldset .jp-inputFieldWrapper select,
.jp-FormGroup-content fieldset .jp-inputFieldWrapper textarea {
  font-size: var(--jp-content-font-size2);
  border-color: var(--jp-input-border-color);
  border-style: solid;
  border-radius: var(--jp-border-radius);
  border-width: 1px;
  padding: 6px 8px;
  background: none;
  color: var(--jp-ui-font-color0);
  height: inherit;
}

.jp-FormGroup-content fieldset input[type='checkbox'] {
  position: relative;
  top: 2px;
  margin-left: 0;
}

.jp-FormGroup-content button.jp-mod-styled {
  cursor: pointer;
}

.jp-FormGroup-content .checkbox label {
  cursor: pointer;
  font-size: var(--jp-content-font-size1);
}

.jp-FormGroup-content .jp-root > fieldset > legend {
  display: none;
}

.jp-FormGroup-content .jp-root > fieldset > p {
  display: none;
}

/** copy of `input.jp-mod-styled:focus` style */
.jp-FormGroup-content fieldset input:focus,
.jp-FormGroup-content fieldset select:focus {
  -moz-outline-radius: unset;
  outline: var(--jp-border-width) solid var(--md-blue-500);
  outline-offset: -1px;
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-FormGroup-content fieldset input:hover:not(:focus),
.jp-FormGroup-content fieldset select:hover:not(:focus) {
  background-color: var(--jp-border-color2);
}

/* stylelint-enable selector-max-type */

.jp-FormGroup-content .checkbox .field-description {
  /* Disable default description field for checkbox:
   because other widgets do not have description fields,
   we add descriptions to each widget on the field level.
  */
  display: none;
}

.jp-FormGroup-content #root__description {
  display: none;
}

.jp-FormGroup-content .jp-modifiedIndicator {
  width: 5px;
  background-color: var(--jp-brand-color2);
  margin-top: 0;
  margin-left: calc(var(--jp-private-settingeditor-modifier-indent) * -1);
  flex-shrink: 0;
}

.jp-FormGroup-content .jp-modifiedIndicator.jp-errorIndicator {
  background-color: var(--jp-error-color0);
  margin-right: 0.5em;
}

/* RJSF ARRAY style */

.jp-arrayFieldWrapper legend {
  font-size: var(--jp-content-font-size2);
  color: var(--jp-ui-font-color0);
  flex-basis: 100%;
  padding: 4px 0;
  font-weight: var(--jp-content-heading-font-weight);
  border-bottom: 1px solid var(--jp-border-color2);
}

.jp-arrayFieldWrapper .field-description {
  padding: 4px 0;
  white-space: pre-wrap;
}

.jp-arrayFieldWrapper .array-item {
  width: 100%;
  border: 1px solid var(--jp-border-color2);
  border-radius: 4px;
  margin: 4px;
}

.jp-ArrayOperations {
  display: flex;
  margin-left: 8px;
}

.jp-ArrayOperationsButton {
  margin: 2px;
}

.jp-ArrayOperationsButton .jp-icon3[fill] {
  fill: var(--jp-ui-font-color0);
}

button.jp-ArrayOperationsButton.jp-mod-styled:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}

/* RJSF form validation error */

.jp-FormGroup-content .validationErrors {
  color: var(--jp-error-color0);
}

/* Hide panel level error as duplicated the field level error */
.jp-FormGroup-content .panel.errors {
  display: none;
}

/* RJSF normal content (settings-editor) */

.jp-FormGroup-contentNormal {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.jp-FormGroup-contentNormal .jp-FormGroup-contentItem {
  margin-left: 7px;
  color: var(--jp-ui-font-color0);
}

.jp-FormGroup-contentNormal .jp-FormGroup-description {
  flex-basis: 100%;
  padding: 4px 7px;
}

.jp-FormGroup-contentNormal .jp-FormGroup-default {
  flex-basis: 100%;
  padding: 4px 7px;
}

.jp-FormGroup-contentNormal .jp-FormGroup-fieldLabel {
  font-size: var(--jp-content-font-size1);
  font-weight: normal;
  min-width: 120px;
}

.jp-FormGroup-contentNormal fieldset:not(:first-child) {
  margin-left: 7px;
}

.jp-FormGroup-contentNormal .field-array-of-string .array-item {
  /* Display `jp-ArrayOperations` buttons side-by-side with content except
    for small screens where flex-wrap will place them one below the other.
  */
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.jp-FormGroup-contentNormal .jp-objectFieldWrapper .form-group {
  padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
  margin-top: 2px;
}

/* RJSF compact content (metadata-form) */

.jp-FormGroup-content.jp-FormGroup-contentCompact {
  width: 100%;
}

.jp-FormGroup-contentCompact .form-group {
  display: flex;
  padding: 0.5em 0.2em 0.5em 0;
}

.jp-FormGroup-contentCompact
  .jp-FormGroup-compactTitle
  .jp-FormGroup-description {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color2);
}

.jp-FormGroup-contentCompact .jp-FormGroup-fieldLabel {
  padding-bottom: 0.3em;
}

.jp-FormGroup-contentCompact .jp-inputFieldWrapper .form-control {
  width: 100%;
  box-sizing: border-box;
}

.jp-FormGroup-contentCompact .jp-arrayFieldWrapper .jp-FormGroup-compactTitle {
  padding-bottom: 7px;
}

.jp-FormGroup-contentCompact
  .jp-objectFieldWrapper
  .jp-objectFieldWrapper
  .form-group {
  padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
  margin-top: 2px;
}

.jp-FormGroup-contentCompact ul.error-detail {
  margin-block-start: 0.5em;
  margin-block-end: 0.5em;
  padding-inline-start: 1em;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-SidePanel {
  display: flex;
  flex-direction: column;
  min-width: var(--jp-sidebar-min-width);
  overflow-y: auto;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  font-size: var(--jp-ui-font-size1);
}

.jp-SidePanel-header {
  flex: 0 0 auto;
  display: flex;
  border-bottom: var(--jp-border-width) solid var(--jp-border-color2);
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin: 0;
  padding: 2px;
  text-transform: uppercase;
}

.jp-SidePanel-toolbar {
  flex: 0 0 auto;
}

.jp-SidePanel-content {
  flex: 1 1 auto;
}

.jp-SidePanel-toolbar,
.jp-AccordionPanel-toolbar {
  height: var(--jp-private-toolbar-height);
}

.jp-SidePanel-toolbar.jp-Toolbar-micro {
  display: none;
}

.lm-AccordionPanel .jp-AccordionPanel-title {
  box-sizing: border-box;
  line-height: 25px;
  margin: 0;
  display: flex;
  align-items: center;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  font-size: var(--jp-ui-font-size0);
}

.jp-AccordionPanel-title {
  cursor: pointer;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  text-transform: uppercase;
}

.lm-AccordionPanel[data-orientation='horizontal'] > .jp-AccordionPanel-title {
  /* Title is rotated for horizontal accordion panel using CSS */
  display: block;
  transform-origin: top left;
  transform: rotate(-90deg) translate(-100%);
}

.jp-AccordionPanel-title .lm-AccordionPanel-titleLabel {
  user-select: none;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}

.jp-AccordionPanel-title .lm-AccordionPanel-titleCollapser {
  transform: rotate(-90deg);
  margin: auto 0;
  height: 16px;
}

.jp-AccordionPanel-title.lm-mod-expanded .lm-AccordionPanel-titleCollapser {
  transform: rotate(0deg);
}

.lm-AccordionPanel .jp-AccordionPanel-toolbar {
  background: none;
  box-shadow: none;
  border: none;
  margin-left: auto;
}

.lm-AccordionPanel .lm-SplitPanel-handle:hover {
  background: var(--jp-layout-color3);
}

.jp-text-truncated {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Spinner {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-layout-color0);
  outline: none;
}

.jp-SpinnerContent {
  font-size: 10px;
  margin: 50px auto;
  text-indent: -9999em;
  width: 3em;
  height: 3em;
  border-radius: 50%;
  background: var(--jp-brand-color3);
  background: linear-gradient(
    to right,
    #f37626 10%,
    rgba(255, 255, 255, 0) 42%
  );
  position: relative;
  animation: load3 1s infinite linear, fadeIn 1s;
}

.jp-SpinnerContent::before {
  width: 50%;
  height: 50%;
  background: #f37626;
  border-radius: 100% 0 0;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
}

.jp-SpinnerContent::after {
  background: var(--jp-layout-color0);
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes load3 {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

button.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: none;
  box-sizing: border-box;
  text-align: center;
  line-height: 32px;
  height: 32px;
  padding: 0 12px;
  letter-spacing: 0.8px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input.jp-mod-styled {
  background: var(--jp-input-background);
  height: 28px;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color1);
  padding-left: 7px;
  padding-right: 7px;
  font-size: var(--jp-ui-font-size2);
  color: var(--jp-ui-font-color0);
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input[type='checkbox'].jp-mod-styled {
  appearance: checkbox;
  -webkit-appearance: checkbox;
  -moz-appearance: checkbox;
  height: auto;
}

input.jp-mod-styled:focus {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-select-wrapper {
  display: flex;
  position: relative;
  flex-direction: column;
  padding: 1px;
  background-color: var(--jp-layout-color1);
  box-sizing: border-box;
  margin-bottom: 12px;
}

.jp-select-wrapper:not(.multiple) {
  height: 28px;
}

.jp-select-wrapper.jp-mod-focused select.jp-mod-styled {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-input-active-background);
}

select.jp-mod-styled:hover {
  cursor: pointer;
  color: var(--jp-ui-font-color0);
  background-color: var(--jp-input-hover-background);
  box-shadow: inset 0 0 1px rgba(0, 0, 0, 0.5);
}

select.jp-mod-styled {
  flex: 1 1 auto;
  width: 100%;
  font-size: var(--jp-ui-font-size2);
  background: var(--jp-input-background);
  color: var(--jp-ui-font-color0);
  padding: 0 25px 0 8px;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

select.jp-mod-styled:not([multiple]) {
  height: 32px;
}

select.jp-mod-styled[multiple] {
  max-height: 200px;
  overflow-y: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-switch {
  display: flex;
  align-items: center;
  padding-left: 4px;
  padding-right: 4px;
  font-size: var(--jp-ui-font-size1);
  background-color: transparent;
  color: var(--jp-ui-font-color1);
  border: none;
  height: 20px;
}

.jp-switch:hover {
  background-color: var(--jp-layout-color2);
}

.jp-switch-label {
  margin-right: 5px;
  font-family: var(--jp-ui-font-family);
}

.jp-switch-track {
  cursor: pointer;
  background-color: var(--jp-switch-color, var(--jp-border-color1));
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 34px;
  height: 16px;
  width: 35px;
  position: relative;
}

.jp-switch-track::before {
  content: '';
  position: absolute;
  height: 10px;
  width: 10px;
  margin: 3px;
  left: 0;
  background-color: var(--jp-ui-inverse-font-color1);
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 50%;
}

.jp-switch[aria-checked='true'] .jp-switch-track {
  background-color: var(--jp-switch-true-position-color, var(--jp-warn-color0));
}

.jp-switch[aria-checked='true'] .jp-switch-track::before {
  /* track width (35) - margins (3 + 3) - thumb width (10) */
  left: 19px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toolbar-height: calc(
    28px + var(--jp-border-width)
  ); /* leave 28px for content */
}

.jp-Toolbar {
  color: var(--jp-ui-font-color1);
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: 2px;
  z-index: 8;
  overflow-x: hidden;
}

/* Toolbar items */

.jp-Toolbar > .jp-Toolbar-item.jp-Toolbar-spacer {
  flex-grow: 1;
  flex-shrink: 1;
}

.jp-Toolbar-item.jp-Toolbar-kernelStatus {
  display: inline-block;
  width: 32px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 16px;
}

.jp-Toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  display: flex;
  padding-left: 1px;
  padding-right: 1px;
  font-size: var(--jp-ui-font-size1);
  line-height: var(--jp-private-toolbar-height);
  height: 100%;
}

/* Toolbar buttons */

/* This is the div we use to wrap the react component into a Widget */
div.jp-ToolbarButton {
  color: transparent;
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0;
  margin: 0;
}

button.jp-ToolbarButtonComponent {
  background: var(--jp-layout-color1);
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0 6px;
  margin: 0;
  height: 24px;
  border-radius: var(--jp-border-radius);
  display: flex;
  align-items: center;
  text-align: center;
  font-size: 14px;
  min-width: unset;
  min-height: unset;
}

button.jp-ToolbarButtonComponent:disabled {
  opacity: 0.4;
}

button.jp-ToolbarButtonComponent > span {
  padding: 0;
  flex: 0 0 auto;
}

button.jp-ToolbarButtonComponent .jp-ToolbarButtonComponent-label {
  font-size: var(--jp-ui-font-size1);
  line-height: 100%;
  padding-left: 2px;
  color: var(--jp-ui-font-color1);
  font-family: var(--jp-ui-font-family);
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar.jp-Toolbar-micro {
  padding: 0;
  min-height: 0;
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar {
  border: none;
  box-shadow: none;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-WindowedPanel-outer {
  position: relative;
  overflow-y: auto;
}

.jp-WindowedPanel-inner {
  position: relative;
}

.jp-WindowedPanel-window {
  position: absolute;
  left: 0;
  right: 0;
  overflow: visible;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Sibling imports */

body {
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
}

/* Disable native link decoration styles everywhere outside of dialog boxes */
a {
  text-decoration: unset;
  color: unset;
}

a:hover {
  text-decoration: unset;
  color: unset;
}

/* Accessibility for links inside dialog box text */
.jp-Dialog-content a {
  text-decoration: revert;
  color: var(--jp-content-link-color);
}

.jp-Dialog-content a:hover {
  text-decoration: revert;
}

/* Styles for ui-components */
.jp-Button {
  color: var(--jp-ui-font-color2);
  border-radius: var(--jp-border-radius);
  padding: 0 12px;
  font-size: var(--jp-ui-font-size1);

  /* Copy from blueprint 3 */
  display: inline-flex;
  flex-direction: row;
  border: none;
  cursor: pointer;
  align-items: center;
  justify-content: center;
  text-align: left;
  vertical-align: middle;
  min-height: 30px;
  min-width: 30px;
}

.jp-Button:disabled {
  cursor: not-allowed;
}

.jp-Button:empty {
  padding: 0 !important;
}

.jp-Button.jp-mod-small {
  min-height: 24px;
  min-width: 24px;
  font-size: 12px;
  padding: 0 7px;
}

/* Use our own theme for hover styles */
.jp-Button.jp-mod-minimal:hover {
  background-color: var(--jp-layout-color2);
}

.jp-Button.jp-mod-minimal {
  background: none;
}

.jp-InputGroup {
  display: block;
  position: relative;
}

.jp-InputGroup input {
  box-sizing: border-box;
  border: none;
  border-radius: 0;
  background-color: transparent;
  color: var(--jp-ui-font-color0);
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
  padding-bottom: 0;
  padding-top: 0;
  padding-left: 10px;
  padding-right: 28px;
  position: relative;
  width: 100%;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  font-size: 14px;
  font-weight: 400;
  height: 30px;
  line-height: 30px;
  outline: none;
  vertical-align: middle;
}

.jp-InputGroup input:focus {
  box-shadow: inset 0 0 0 var(--jp-border-width)
      var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-InputGroup input:disabled {
  cursor: not-allowed;
  resize: block;
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color2);
}

.jp-InputGroup input:disabled ~ span {
  cursor: not-allowed;
  color: var(--jp-ui-font-color2);
}

.jp-InputGroup input::placeholder,
input::placeholder {
  color: var(--jp-ui-font-color2);
}

.jp-InputGroupAction {
  position: absolute;
  bottom: 1px;
  right: 0;
  padding: 6px;
}

.jp-HTMLSelect.jp-DefaultStyle select {
  background-color: initial;
  border: none;
  border-radius: 0;
  box-shadow: none;
  color: var(--jp-ui-font-color0);
  display: block;
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  height: 24px;
  line-height: 14px;
  padding: 0 25px 0 10px;
  text-align: left;
  -moz-appearance: none;
  -webkit-appearance: none;
}

.jp-HTMLSelect.jp-DefaultStyle select:disabled {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color2);
  cursor: not-allowed;
  resize: block;
}

.jp-HTMLSelect.jp-DefaultStyle select:disabled ~ span {
  cursor: not-allowed;
}

/* Use our own theme for hover and option styles */
/* stylelint-disable-next-line selector-max-type */
.jp-HTMLSelect.jp-DefaultStyle select:hover,
.jp-HTMLSelect.jp-DefaultStyle select > option {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color0);
}

select {
  box-sizing: border-box;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-StatusBar-Widget {
  display: flex;
  align-items: center;
  background: var(--jp-layout-color2);
  min-height: var(--jp-statusbar-height);
  justify-content: space-between;
  padding: 0 10px;
}

.jp-StatusBar-Left {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.jp-StatusBar-Middle {
  display: flex;
  align-items: center;
}

.jp-StatusBar-Right {
  display: flex;
  align-items: center;
  flex-direction: row-reverse;
}

.jp-StatusBar-Item {
  max-height: var(--jp-statusbar-height);
  margin: 0 2px;
  height: var(--jp-statusbar-height);
  white-space: nowrap;
  text-overflow: ellipsis;
  color: var(--jp-ui-font-color1);
  padding: 0 6px;
}

.jp-mod-highlighted:hover {
  background-color: var(--jp-layout-color3);
}

.jp-mod-clicked {
  background-color: var(--jp-brand-color1);
}

.jp-mod-clicked:hover {
  background-color: var(--jp-brand-color0);
}

.jp-mod-clicked .jp-StatusBar-TextItem {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-StatusBar-HoverItem {
  box-shadow: '0px 4px 4px rgba(0, 0, 0, 0.25)';
}

.jp-StatusBar-TextItem {
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  line-height: 24px;
  color: var(--jp-ui-font-color1);
}

.jp-StatusBar-GroupItem {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.jp-Statusbar-ProgressCircle svg {
  display: block;
  margin: 0 auto;
  width: 16px;
  height: 24px;
  align-self: normal;
}

.jp-Statusbar-ProgressCircle path {
  fill: var(--jp-inverse-layout-color3);
}

.jp-Statusbar-ProgressBar-progress-bar {
  height: 10px;
  width: 100px;
  border: solid 0.25px var(--jp-brand-color2);
  border-radius: 3px;
  overflow: hidden;
  align-self: center;
}

.jp-Statusbar-ProgressBar-progress-bar > div {
  background-color: var(--jp-brand-color2);
  background-image: linear-gradient(
    -45deg,
    rgba(255, 255, 255, 0.2) 25%,
    transparent 25%,
    transparent 50%,
    rgba(255, 255, 255, 0.2) 50%,
    rgba(255, 255, 255, 0.2) 75%,
    transparent 75%,
    transparent
  );
  background-size: 40px 40px;
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 14px;
  color: #fff;
  text-align: center;
  animation: jp-Statusbar-ExecutionTime-progress-bar 2s linear infinite;
}

.jp-Statusbar-ProgressBar-progress-bar p {
  color: var(--jp-ui-font-color1);
  font-family: var(--jp-ui-font-family);
  font-size: var(--jp-ui-font-size1);
  line-height: 10px;
  width: 100px;
}

@keyframes jp-Statusbar-ExecutionTime-progress-bar {
  0% {
    background-position: 0 0;
  }

  100% {
    background-position: 40px 40px;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-commandpalette-search-height: 28px;
}

/*-----------------------------------------------------------------------------
| Overall styles
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  padding-bottom: 0;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);

  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Modal variant
|----------------------------------------------------------------------------*/

.jp-ModalCommandPalette {
  position: absolute;
  z-index: 10000;
  top: 38px;
  left: 30%;
  margin: 0;
  padding: 4px;
  width: 40%;
  box-shadow: var(--jp-elevation-z4);
  border-radius: 4px;
  background: var(--jp-layout-color0);
}

.jp-ModalCommandPalette .lm-CommandPalette {
  max-height: 40vh;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-close-icon::after {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-header {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-item {
  margin-left: 4px;
  margin-right: 4px;
}

.jp-ModalCommandPalette
  .lm-CommandPalette
  .lm-CommandPalette-item.lm-mod-disabled {
  display: none;
}

/*-----------------------------------------------------------------------------
| Search
|----------------------------------------------------------------------------*/

.lm-CommandPalette-search {
  padding: 4px;
  background-color: var(--jp-layout-color1);
  z-index: 2;
}

.lm-CommandPalette-wrapper {
  overflow: overlay;
  padding: 0 9px;
  background-color: var(--jp-input-active-background);
  height: 30px;
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.lm-CommandPalette.lm-mod-focused .lm-CommandPalette-wrapper {
  box-shadow: inset 0 0 0 1px var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-SearchIconGroup {
  color: white;
  background-color: var(--jp-brand-color1);
  position: absolute;
  top: 4px;
  right: 4px;
  padding: 5px 5px 1px;
}

.jp-SearchIconGroup svg {
  height: 20px;
  width: 20px;
}

.jp-SearchIconGroup .jp-icon3[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-input {
  background: transparent;
  width: calc(100% - 18px);
  float: left;
  border: none;
  outline: none;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  line-height: var(--jp-private-commandpalette-search-height);
}

.lm-CommandPalette-input::-webkit-input-placeholder,
.lm-CommandPalette-input::-moz-placeholder,
.lm-CommandPalette-input:-ms-input-placeholder {
  color: var(--jp-ui-font-color2);
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Results
|----------------------------------------------------------------------------*/

.lm-CommandPalette-header:first-child {
  margin-top: 0;
}

.lm-CommandPalette-header {
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin-top: 8px;
  padding: 8px 0 8px 12px;
  text-transform: uppercase;
}

.lm-CommandPalette-header.lm-mod-active {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-header > mark {
  background-color: transparent;
  font-weight: bold;
  color: var(--jp-ui-font-color1);
}

.lm-CommandPalette-item {
  padding: 4px 12px 4px 4px;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  font-weight: 400;
  display: flex;
}

.lm-CommandPalette-item.lm-mod-disabled {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item.lm-mod-active {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-inverse-font-color0);
}

.lm-CommandPalette-item.lm-mod-active .jp-icon-selectable[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-item.lm-mod-active:hover:not(.lm-mod-disabled) {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item:hover:not(.lm-mod-active):not(.lm-mod-disabled) {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-itemContent {
  overflow: hidden;
}

.lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.lm-CommandPalette-item.lm-mod-disabled mark {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item .lm-CommandPalette-itemIcon {
  margin: 0 4px 0 0;
  position: relative;
  width: 16px;
  top: 2px;
  flex: 0 0 auto;
}

.lm-CommandPalette-item.lm-mod-disabled .lm-CommandPalette-itemIcon {
  opacity: 0.6;
}

.lm-CommandPalette-item .lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemCaption {
  display: none;
}

.lm-CommandPalette-content {
  background-color: var(--jp-layout-color1);
}

.lm-CommandPalette-content:empty::after {
  content: 'No results';
  margin: auto;
  margin-top: 20px;
  width: 100px;
  display: block;
  font-size: var(--jp-ui-font-size2);
  font-family: var(--jp-ui-font-family);
  font-weight: lighter;
}

.lm-CommandPalette-emptyMessage {
  text-align: center;
  margin-top: 24px;
  line-height: 1.32;
  padding: 0 8px;
  color: var(--jp-content-font-color3);
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Dialog {
  position: absolute;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  top: 0;
  left: 0;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-dialog-background);
}

.jp-Dialog-content {
  display: flex;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  background: var(--jp-layout-color1);
  padding: 24px 24px 12px;
  min-width: 300px;
  min-height: 150px;
  max-width: 1000px;
  max-height: 500px;
  box-sizing: border-box;
  box-shadow: var(--jp-elevation-z20);
  word-wrap: break-word;
  border-radius: var(--jp-border-radius);

  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color1);
  resize: both;
}

.jp-Dialog-content.jp-Dialog-content-small {
  max-width: 500px;
}

.jp-Dialog-button {
  overflow: visible;
}

button.jp-Dialog-button:focus {
  outline: 1px solid var(--jp-brand-color1);
  outline-offset: 4px;
  -moz-outline-radius: 0;
}

button.jp-Dialog-button:focus::-moz-focus-inner {
  border: 0;
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus,
button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus,
button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
  outline-offset: 4px;
  -moz-outline-radius: 0;
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus {
  outline: 1px solid var(--jp-accept-color-normal, var(--jp-brand-color1));
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus {
  outline: 1px solid var(--jp-warn-color-normal, var(--jp-error-color1));
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
  outline: 1px solid var(--jp-reject-color-normal, var(--md-grey-600));
}

button.jp-Dialog-close-button {
  padding: 0;
  height: 100%;
  min-width: unset;
  min-height: unset;
}

.jp-Dialog-header {
  display: flex;
  justify-content: space-between;
  flex: 0 0 auto;
  padding-bottom: 12px;
  font-size: var(--jp-ui-font-size3);
  font-weight: 400;
  color: var(--jp-ui-font-color1);
}

.jp-Dialog-body {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
  font-size: var(--jp-ui-font-size1);
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

.jp-Dialog-footer {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  flex: 0 0 auto;
  margin-left: -12px;
  margin-right: -12px;
  padding: 12px;
}

.jp-Dialog-checkbox {
  padding-right: 5px;
}

.jp-Dialog-checkbox > input:focus-visible {
  outline: 1px solid var(--jp-input-active-border-color);
  outline-offset: 1px;
}

.jp-Dialog-spacer {
  flex: 1 1 auto;
}

.jp-Dialog-title {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.jp-Dialog-body > .jp-select-wrapper {
  width: 100%;
}

.jp-Dialog-body > button {
  padding: 0 16px;
}

.jp-Dialog-body > label {
  line-height: 1.4;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-button.jp-mod-styled:not(:last-child) {
  margin-right: 12px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-Input-Boolean-Dialog {
  flex-direction: row-reverse;
  align-items: end;
  width: 100%;
}

.jp-Input-Boolean-Dialog > label {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MainAreaWidget > :focus {
  outline: none;
}

.jp-MainAreaWidget .jp-MainAreaWidget-error {
  padding: 6px;
}

.jp-MainAreaWidget .jp-MainAreaWidget-error > pre {
  width: auto;
  padding: 10px;
  background: var(--jp-error-color3);
  border: var(--jp-border-width) solid var(--jp-error-color1);
  border-radius: var(--jp-border-radius);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  white-space: pre-wrap;
  word-wrap: break-word;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/**
 * google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 */
:root {
  --md-red-50: #ffebee;
  --md-red-100: #ffcdd2;
  --md-red-200: #ef9a9a;
  --md-red-300: #e57373;
  --md-red-400: #ef5350;
  --md-red-500: #f44336;
  --md-red-600: #e53935;
  --md-red-700: #d32f2f;
  --md-red-800: #c62828;
  --md-red-900: #b71c1c;
  --md-red-A100: #ff8a80;
  --md-red-A200: #ff5252;
  --md-red-A400: #ff1744;
  --md-red-A700: #d50000;
  --md-pink-50: #fce4ec;
  --md-pink-100: #f8bbd0;
  --md-pink-200: #f48fb1;
  --md-pink-300: #f06292;
  --md-pink-400: #ec407a;
  --md-pink-500: #e91e63;
  --md-pink-600: #d81b60;
  --md-pink-700: #c2185b;
  --md-pink-800: #ad1457;
  --md-pink-900: #880e4f;
  --md-pink-A100: #ff80ab;
  --md-pink-A200: #ff4081;
  --md-pink-A400: #f50057;
  --md-pink-A700: #c51162;
  --md-purple-50: #f3e5f5;
  --md-purple-100: #e1bee7;
  --md-purple-200: #ce93d8;
  --md-purple-300: #ba68c8;
  --md-purple-400: #ab47bc;
  --md-purple-500: #9c27b0;
  --md-purple-600: #8e24aa;
  --md-purple-700: #7b1fa2;
  --md-purple-800: #6a1b9a;
  --md-purple-900: #4a148c;
  --md-purple-A100: #ea80fc;
  --md-purple-A200: #e040fb;
  --md-purple-A400: #d500f9;
  --md-purple-A700: #a0f;
  --md-deep-purple-50: #ede7f6;
  --md-deep-purple-100: #d1c4e9;
  --md-deep-purple-200: #b39ddb;
  --md-deep-purple-300: #9575cd;
  --md-deep-purple-400: #7e57c2;
  --md-deep-purple-500: #673ab7;
  --md-deep-purple-600: #5e35b1;
  --md-deep-purple-700: #512da8;
  --md-deep-purple-800: #4527a0;
  --md-deep-purple-900: #311b92;
  --md-deep-purple-A100: #b388ff;
  --md-deep-purple-A200: #7c4dff;
  --md-deep-purple-A400: #651fff;
  --md-deep-purple-A700: #6200ea;
  --md-indigo-50: #e8eaf6;
  --md-indigo-100: #c5cae9;
  --md-indigo-200: #9fa8da;
  --md-indigo-300: #7986cb;
  --md-indigo-400: #5c6bc0;
  --md-indigo-500: #3f51b5;
  --md-indigo-600: #3949ab;
  --md-indigo-700: #303f9f;
  --md-indigo-800: #283593;
  --md-indigo-900: #1a237e;
  --md-indigo-A100: #8c9eff;
  --md-indigo-A200: #536dfe;
  --md-indigo-A400: #3d5afe;
  --md-indigo-A700: #304ffe;
  --md-blue-50: #e3f2fd;
  --md-blue-100: #bbdefb;
  --md-blue-200: #90caf9;
  --md-blue-300: #64b5f6;
  --md-blue-400: #42a5f5;
  --md-blue-500: #2196f3;
  --md-blue-600: #1e88e5;
  --md-blue-700: #1976d2;
  --md-blue-800: #1565c0;
  --md-blue-900: #0d47a1;
  --md-blue-A100: #82b1ff;
  --md-blue-A200: #448aff;
  --md-blue-A400: #2979ff;
  --md-blue-A700: #2962ff;
  --md-light-blue-50: #e1f5fe;
  --md-light-blue-100: #b3e5fc;
  --md-light-blue-200: #81d4fa;
  --md-light-blue-300: #4fc3f7;
  --md-light-blue-400: #29b6f6;
  --md-light-blue-500: #03a9f4;
  --md-light-blue-600: #039be5;
  --md-light-blue-700: #0288d1;
  --md-light-blue-800: #0277bd;
  --md-light-blue-900: #01579b;
  --md-light-blue-A100: #80d8ff;
  --md-light-blue-A200: #40c4ff;
  --md-light-blue-A400: #00b0ff;
  --md-light-blue-A700: #0091ea;
  --md-cyan-50: #e0f7fa;
  --md-cyan-100: #b2ebf2;
  --md-cyan-200: #80deea;
  --md-cyan-300: #4dd0e1;
  --md-cyan-400: #26c6da;
  --md-cyan-500: #00bcd4;
  --md-cyan-600: #00acc1;
  --md-cyan-700: #0097a7;
  --md-cyan-800: #00838f;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84ffff;
  --md-cyan-A200: #18ffff;
  --md-cyan-A400: #00e5ff;
  --md-cyan-A700: #00b8d4;
  --md-teal-50: #e0f2f1;
  --md-teal-100: #b2dfdb;
  --md-teal-200: #80cbc4;
  --md-teal-300: #4db6ac;
  --md-teal-400: #26a69a;
  --md-teal-500: #009688;
  --md-teal-600: #00897b;
  --md-teal-700: #00796b;
  --md-teal-800: #00695c;
  --md-teal-900: #004d40;
  --md-teal-A100: #a7ffeb;
  --md-teal-A200: #64ffda;
  --md-teal-A400: #1de9b6;
  --md-teal-A700: #00bfa5;
  --md-green-50: #e8f5e9;
  --md-green-100: #c8e6c9;
  --md-green-200: #a5d6a7;
  --md-green-300: #81c784;
  --md-green-400: #66bb6a;
  --md-green-500: #4caf50;
  --md-green-600: #43a047;
  --md-green-700: #388e3c;
  --md-green-800: #2e7d32;
  --md-green-900: #1b5e20;
  --md-green-A100: #b9f6ca;
  --md-green-A200: #69f0ae;
  --md-green-A400: #00e676;
  --md-green-A700: #00c853;
  --md-light-green-50: #f1f8e9;
  --md-light-green-100: #dcedc8;
  --md-light-green-200: #c5e1a5;
  --md-light-green-300: #aed581;
  --md-light-green-400: #9ccc65;
  --md-light-green-500: #8bc34a;
  --md-light-green-600: #7cb342;
  --md-light-green-700: #689f38;
  --md-light-green-800: #558b2f;
  --md-light-green-900: #33691e;
  --md-light-green-A100: #ccff90;
  --md-light-green-A200: #b2ff59;
  --md-light-green-A400: #76ff03;
  --md-light-green-A700: #64dd17;
  --md-lime-50: #f9fbe7;
  --md-lime-100: #f0f4c3;
  --md-lime-200: #e6ee9c;
  --md-lime-300: #dce775;
  --md-lime-400: #d4e157;
  --md-lime-500: #cddc39;
  --md-lime-600: #c0ca33;
  --md-lime-700: #afb42b;
  --md-lime-800: #9e9d24;
  --md-lime-900: #827717;
  --md-lime-A100: #f4ff81;
  --md-lime-A200: #eeff41;
  --md-lime-A400: #c6ff00;
  --md-lime-A700: #aeea00;
  --md-yellow-50: #fffde7;
  --md-yellow-100: #fff9c4;
  --md-yellow-200: #fff59d;
  --md-yellow-300: #fff176;
  --md-yellow-400: #ffee58;
  --md-yellow-500: #ffeb3b;
  --md-yellow-600: #fdd835;
  --md-yellow-700: #fbc02d;
  --md-yellow-800: #f9a825;
  --md-yellow-900: #f57f17;
  --md-yellow-A100: #ffff8d;
  --md-yellow-A200: #ff0;
  --md-yellow-A400: #ffea00;
  --md-yellow-A700: #ffd600;
  --md-amber-50: #fff8e1;
  --md-amber-100: #ffecb3;
  --md-amber-200: #ffe082;
  --md-amber-300: #ffd54f;
  --md-amber-400: #ffca28;
  --md-amber-500: #ffc107;
  --md-amber-600: #ffb300;
  --md-amber-700: #ffa000;
  --md-amber-800: #ff8f00;
  --md-amber-900: #ff6f00;
  --md-amber-A100: #ffe57f;
  --md-amber-A200: #ffd740;
  --md-amber-A400: #ffc400;
  --md-amber-A700: #ffab00;
  --md-orange-50: #fff3e0;
  --md-orange-100: #ffe0b2;
  --md-orange-200: #ffcc80;
  --md-orange-300: #ffb74d;
  --md-orange-400: #ffa726;
  --md-orange-500: #ff9800;
  --md-orange-600: #fb8c00;
  --md-orange-700: #f57c00;
  --md-orange-800: #ef6c00;
  --md-orange-900: #e65100;
  --md-orange-A100: #ffd180;
  --md-orange-A200: #ffab40;
  --md-orange-A400: #ff9100;
  --md-orange-A700: #ff6d00;
  --md-deep-orange-50: #fbe9e7;
  --md-deep-orange-100: #ffccbc;
  --md-deep-orange-200: #ffab91;
  --md-deep-orange-300: #ff8a65;
  --md-deep-orange-400: #ff7043;
  --md-deep-orange-500: #ff5722;
  --md-deep-orange-600: #f4511e;
  --md-deep-orange-700: #e64a19;
  --md-deep-orange-800: #d84315;
  --md-deep-orange-900: #bf360c;
  --md-deep-orange-A100: #ff9e80;
  --md-deep-orange-A200: #ff6e40;
  --md-deep-orange-A400: #ff3d00;
  --md-deep-orange-A700: #dd2c00;
  --md-brown-50: #efebe9;
  --md-brown-100: #d7ccc8;
  --md-brown-200: #bcaaa4;
  --md-brown-300: #a1887f;
  --md-brown-400: #8d6e63;
  --md-brown-500: #795548;
  --md-brown-600: #6d4c41;
  --md-brown-700: #5d4037;
  --md-brown-800: #4e342e;
  --md-brown-900: #3e2723;
  --md-grey-50: #fafafa;
  --md-grey-100: #f5f5f5;
  --md-grey-200: #eee;
  --md-grey-300: #e0e0e0;
  --md-grey-400: #bdbdbd;
  --md-grey-500: #9e9e9e;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;
  --md-blue-grey-50: #eceff1;
  --md-blue-grey-100: #cfd8dc;
  --md-blue-grey-200: #b0bec5;
  --md-blue-grey-300: #90a4ae;
  --md-blue-grey-400: #78909c;
  --md-blue-grey-500: #607d8b;
  --md-blue-grey-600: #546e7a;
  --md-blue-grey-700: #455a64;
  --md-blue-grey-800: #37474f;
  --md-blue-grey-900: #263238;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| RenderedText
|----------------------------------------------------------------------------*/

:root {
  /* This is the padding value to fill the gaps between lines containing spans with background color. */
  --jp-private-code-span-padding: calc(
    (var(--jp-code-line-height) - 1) * var(--jp-code-font-size) / 2
  );
}

.jp-RenderedText {
  text-align: left;
  padding-left: var(--jp-code-padding);
  line-height: var(--jp-code-line-height);
  font-family: var(--jp-code-font-family);
}

.jp-RenderedText pre,
.jp-RenderedJavaScript pre,
.jp-RenderedHTMLCommon pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
  border: none;
  margin: 0;
  padding: 0;
}

.jp-RenderedText pre a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedText pre a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedText pre a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* console foregrounds and backgrounds */
.jp-RenderedText pre .ansi-black-fg {
  color: #3e424d;
}

.jp-RenderedText pre .ansi-red-fg {
  color: #e75c58;
}

.jp-RenderedText pre .ansi-green-fg {
  color: #00a250;
}

.jp-RenderedText pre .ansi-yellow-fg {
  color: #ddb62b;
}

.jp-RenderedText pre .ansi-blue-fg {
  color: #208ffb;
}

.jp-RenderedText pre .ansi-magenta-fg {
  color: #d160c4;
}

.jp-RenderedText pre .ansi-cyan-fg {
  color: #60c6c8;
}

.jp-RenderedText pre .ansi-white-fg {
  color: #c5c1b4;
}

.jp-RenderedText pre .ansi-black-bg {
  background-color: #3e424d;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-red-bg {
  background-color: #e75c58;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-green-bg {
  background-color: #00a250;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-yellow-bg {
  background-color: #ddb62b;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-blue-bg {
  background-color: #208ffb;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-magenta-bg {
  background-color: #d160c4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-cyan-bg {
  background-color: #60c6c8;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-white-bg {
  background-color: #c5c1b4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-black-intense-fg {
  color: #282c36;
}

.jp-RenderedText pre .ansi-red-intense-fg {
  color: #b22b31;
}

.jp-RenderedText pre .ansi-green-intense-fg {
  color: #007427;
}

.jp-RenderedText pre .ansi-yellow-intense-fg {
  color: #b27d12;
}

.jp-RenderedText pre .ansi-blue-intense-fg {
  color: #0065ca;
}

.jp-RenderedText pre .ansi-magenta-intense-fg {
  color: #a03196;
}

.jp-RenderedText pre .ansi-cyan-intense-fg {
  color: #258f8f;
}

.jp-RenderedText pre .ansi-white-intense-fg {
  color: #a1a6b2;
}

.jp-RenderedText pre .ansi-black-intense-bg {
  background-color: #282c36;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-red-intense-bg {
  background-color: #b22b31;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-green-intense-bg {
  background-color: #007427;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-yellow-intense-bg {
  background-color: #b27d12;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-blue-intense-bg {
  background-color: #0065ca;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-magenta-intense-bg {
  background-color: #a03196;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-cyan-intense-bg {
  background-color: #258f8f;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-white-intense-bg {
  background-color: #a1a6b2;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-default-inverse-fg {
  color: var(--jp-ui-inverse-font-color0);
}

.jp-RenderedText pre .ansi-default-inverse-bg {
  background-color: var(--jp-inverse-layout-color0);
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-bold {
  font-weight: bold;
}

.jp-RenderedText pre .ansi-underline {
  text-decoration: underline;
}

.jp-RenderedText[data-mime-type='application/vnd.jupyter.stderr'] {
  background: var(--jp-rendermime-error-background);
  padding-top: var(--jp-code-padding);
}

/*-----------------------------------------------------------------------------
| RenderedLatex
|----------------------------------------------------------------------------*/

.jp-RenderedLatex {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
}

/* Left-justify outputs.*/
.jp-OutputArea-output.jp-RenderedLatex {
  padding: var(--jp-code-padding);
  text-align: left;
}

/*-----------------------------------------------------------------------------
| RenderedHTML
|----------------------------------------------------------------------------*/

.jp-RenderedHTMLCommon {
  color: var(--jp-content-font-color1);
  font-family: var(--jp-content-font-family);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);

  /* Give a bit more R padding on Markdown text to keep line lengths reasonable */
  padding-right: 20px;
}

.jp-RenderedHTMLCommon em {
  font-style: italic;
}

.jp-RenderedHTMLCommon strong {
  font-weight: bold;
}

.jp-RenderedHTMLCommon u {
  text-decoration: underline;
}

.jp-RenderedHTMLCommon a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* Headings */

.jp-RenderedHTMLCommon h1,
.jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3,
.jp-RenderedHTMLCommon h4,
.jp-RenderedHTMLCommon h5,
.jp-RenderedHTMLCommon h6 {
  line-height: var(--jp-content-heading-line-height);
  font-weight: var(--jp-content-heading-font-weight);
  font-style: normal;
  margin: var(--jp-content-heading-margin-top) 0
    var(--jp-content-heading-margin-bottom) 0;
}

.jp-RenderedHTMLCommon h1:first-child,
.jp-RenderedHTMLCommon h2:first-child,
.jp-RenderedHTMLCommon h3:first-child,
.jp-RenderedHTMLCommon h4:first-child,
.jp-RenderedHTMLCommon h5:first-child,
.jp-RenderedHTMLCommon h6:first-child {
  margin-top: calc(0.5 * var(--jp-content-heading-margin-top));
}

.jp-RenderedHTMLCommon h1:last-child,
.jp-RenderedHTMLCommon h2:last-child,
.jp-RenderedHTMLCommon h3:last-child,
.jp-RenderedHTMLCommon h4:last-child,
.jp-RenderedHTMLCommon h5:last-child,
.jp-RenderedHTMLCommon h6:last-child {
  margin-bottom: calc(0.5 * var(--jp-content-heading-margin-bottom));
}

.jp-RenderedHTMLCommon h1 {
  font-size: var(--jp-content-font-size5);
}

.jp-RenderedHTMLCommon h2 {
  font-size: var(--jp-content-font-size4);
}

.jp-RenderedHTMLCommon h3 {
  font-size: var(--jp-content-font-size3);
}

.jp-RenderedHTMLCommon h4 {
  font-size: var(--jp-content-font-size2);
}

.jp-RenderedHTMLCommon h5 {
  font-size: var(--jp-content-font-size1);
}

.jp-RenderedHTMLCommon h6 {
  font-size: var(--jp-content-font-size0);
}

/* Lists */

/* stylelint-disable selector-max-type, selector-max-compound-selectors */

.jp-RenderedHTMLCommon ul:not(.list-inline),
.jp-RenderedHTMLCommon ol:not(.list-inline) {
  padding-left: 2em;
}

.jp-RenderedHTMLCommon ul {
  list-style: disc;
}

.jp-RenderedHTMLCommon ul ul {
  list-style: square;
}

.jp-RenderedHTMLCommon ul ul ul {
  list-style: circle;
}

.jp-RenderedHTMLCommon ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol ol {
  list-style: upper-alpha;
}

.jp-RenderedHTMLCommon ol ol ol {
  list-style: lower-alpha;
}

.jp-RenderedHTMLCommon ol ol ol ol {
  list-style: lower-roman;
}

.jp-RenderedHTMLCommon ol ol ol ol ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol,
.jp-RenderedHTMLCommon ul {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon ul ul,
.jp-RenderedHTMLCommon ul ol,
.jp-RenderedHTMLCommon ol ul,
.jp-RenderedHTMLCommon ol ol {
  margin-bottom: 0;
}

/* stylelint-enable selector-max-type, selector-max-compound-selectors */

.jp-RenderedHTMLCommon hr {
  color: var(--jp-border-color2);
  background-color: var(--jp-border-color1);
  margin-top: 1em;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon > pre {
  margin: 1.5em 2em;
}

.jp-RenderedHTMLCommon pre,
.jp-RenderedHTMLCommon code {
  border: 0;
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  line-height: var(--jp-code-line-height);
  padding: 0;
  white-space: pre-wrap;
}

.jp-RenderedHTMLCommon :not(pre) > code {
  background-color: var(--jp-layout-color2);
  padding: 1px 5px;
}

/* Tables */

.jp-RenderedHTMLCommon table {
  border-collapse: collapse;
  border-spacing: 0;
  border: none;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  table-layout: fixed;
  margin-left: auto;
  margin-bottom: 1em;
  margin-right: auto;
}

.jp-RenderedHTMLCommon thead {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  vertical-align: bottom;
}

.jp-RenderedHTMLCommon td,
.jp-RenderedHTMLCommon th,
.jp-RenderedHTMLCommon tr {
  vertical-align: middle;
  padding: 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}

.jp-RenderedMarkdown.jp-RenderedHTMLCommon td,
.jp-RenderedMarkdown.jp-RenderedHTMLCommon th {
  max-width: none;
}

:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon td,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon th,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon tr {
  text-align: right;
}

.jp-RenderedHTMLCommon th {
  font-weight: bold;
}

.jp-RenderedHTMLCommon tbody tr:nth-child(odd) {
  background: var(--jp-layout-color0);
}

.jp-RenderedHTMLCommon tbody tr:nth-child(even) {
  background: var(--jp-rendermime-table-row-background);
}

.jp-RenderedHTMLCommon tbody tr:hover {
  background: var(--jp-rendermime-table-row-hover-background);
}

.jp-RenderedHTMLCommon p {
  text-align: left;
  margin: 0;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon img {
  -moz-force-broken-image-icon: 1;
}

/* Restrict to direct children as other images could be nested in other content. */
.jp-RenderedHTMLCommon > img {
  display: block;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 1em;
}

/* Change color behind transparent images if they need it... */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-light-background {
  background-color: var(--jp-inverse-layout-color1);
}

[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-dark-background {
  background-color: var(--jp-inverse-layout-color1);
}

.jp-RenderedHTMLCommon img,
.jp-RenderedImage img,
.jp-RenderedHTMLCommon svg,
.jp-RenderedSVG svg {
  max-width: 100%;
  height: auto;
}

.jp-RenderedHTMLCommon img.jp-mod-unconfined,
.jp-RenderedImage img.jp-mod-unconfined,
.jp-RenderedHTMLCommon svg.jp-mod-unconfined,
.jp-RenderedSVG svg.jp-mod-unconfined {
  max-width: none;
}

.jp-RenderedHTMLCommon .alert {
  padding: var(--jp-notebook-padding);
  border: var(--jp-border-width) solid transparent;
  border-radius: var(--jp-border-radius);
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon .alert-info {
  color: var(--jp-info-color0);
  background-color: var(--jp-info-color3);
  border-color: var(--jp-info-color2);
}

.jp-RenderedHTMLCommon .alert-info hr {
  border-color: var(--jp-info-color3);
}

.jp-RenderedHTMLCommon .alert-info > p:last-child,
.jp-RenderedHTMLCommon .alert-info > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-warning {
  color: var(--jp-warn-color0);
  background-color: var(--jp-warn-color3);
  border-color: var(--jp-warn-color2);
}

.jp-RenderedHTMLCommon .alert-warning hr {
  border-color: var(--jp-warn-color3);
}

.jp-RenderedHTMLCommon .alert-warning > p:last-child,
.jp-RenderedHTMLCommon .alert-warning > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-success {
  color: var(--jp-success-color0);
  background-color: var(--jp-success-color3);
  border-color: var(--jp-success-color2);
}

.jp-RenderedHTMLCommon .alert-success hr {
  border-color: var(--jp-success-color3);
}

.jp-RenderedHTMLCommon .alert-success > p:last-child,
.jp-RenderedHTMLCommon .alert-success > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-danger {
  color: var(--jp-error-color0);
  background-color: var(--jp-error-color3);
  border-color: var(--jp-error-color2);
}

.jp-RenderedHTMLCommon .alert-danger hr {
  border-color: var(--jp-error-color3);
}

.jp-RenderedHTMLCommon .alert-danger > p:last-child,
.jp-RenderedHTMLCommon .alert-danger > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon blockquote {
  margin: 1em 2em;
  padding: 0 1em;
  border-left: 5px solid var(--jp-border-color2);
}

a.jp-InternalAnchorLink {
  visibility: hidden;
  margin-left: 8px;
  color: var(--md-blue-800);
}

h1:hover .jp-InternalAnchorLink,
h2:hover .jp-InternalAnchorLink,
h3:hover .jp-InternalAnchorLink,
h4:hover .jp-InternalAnchorLink,
h5:hover .jp-InternalAnchorLink,
h6:hover .jp-InternalAnchorLink {
  visibility: visible;
}

.jp-RenderedHTMLCommon kbd {
  background-color: var(--jp-rendermime-table-row-background);
  border: 1px solid var(--jp-border-color0);
  border-bottom-color: var(--jp-border-color2);
  border-radius: 3px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
  display: inline-block;
  font-size: var(--jp-ui-font-size0);
  line-height: 1em;
  padding: 0.2em 0.5em;
}

/* Most direct children of .jp-RenderedHTMLCommon have a margin-bottom of 1.0.
 * At the bottom of cells this is a bit too much as there is also spacing
 * between cells. Going all the way to 0 gets too tight between markdown and
 * code cells.
 */
.jp-RenderedHTMLCommon > *:last-child {
  margin-bottom: 0.5em;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-cursor-backdrop {
  position: fixed;
  width: 200px;
  height: 200px;
  margin-top: -100px;
  margin-left: -100px;
  will-change: transform;
  z-index: 100;
}

.lm-mod-drag-image {
  will-change: transform;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-lineFormSearch {
  padding: 4px 12px;
  background-color: var(--jp-layout-color2);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
  font-size: var(--jp-ui-font-size1);
}

.jp-lineFormCaption {
  font-size: var(--jp-ui-font-size0);
  line-height: var(--jp-ui-font-size1);
  margin-top: 4px;
  color: var(--jp-ui-font-color0);
}

.jp-baseLineForm {
  border: none;
  border-radius: 0;
  position: absolute;
  background-size: 16px;
  background-repeat: no-repeat;
  background-position: center;
  outline: none;
}

.jp-lineFormButtonContainer {
  top: 4px;
  right: 8px;
  height: 24px;
  padding: 0 12px;
  width: 12px;
}

.jp-lineFormButtonIcon {
  top: 0;
  right: 0;
  background-color: var(--jp-brand-color1);
  height: 100%;
  width: 100%;
  box-sizing: border-box;
  padding: 4px 6px;
}

.jp-lineFormButton {
  top: 0;
  right: 0;
  background-color: transparent;
  height: 100%;
  width: 100%;
  box-sizing: border-box;
}

.jp-lineFormWrapper {
  overflow: hidden;
  padding: 0 8px;
  border: 1px solid var(--jp-border-color0);
  background-color: var(--jp-input-active-background);
  height: 22px;
}

.jp-lineFormWrapperFocusWithin {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-lineFormInput {
  background: transparent;
  width: 200px;
  height: 100%;
  border: none;
  outline: none;
  color: var(--jp-ui-font-color0);
  line-height: 28px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-JSONEditor {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.jp-JSONEditor-host {
  flex: 1 1 auto;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0;
  background: var(--jp-layout-color0);
  min-height: 50px;
  padding: 1px;
}

.jp-JSONEditor.jp-mod-error .jp-JSONEditor-host {
  border-color: red;
  outline-color: red;
}

.jp-JSONEditor-header {
  display: flex;
  flex: 1 0 auto;
  padding: 0 0 0 12px;
}

.jp-JSONEditor-header label {
  flex: 0 0 auto;
}

.jp-JSONEditor-commitButton {
  height: 16px;
  width: 16px;
  background-size: 18px;
  background-repeat: no-repeat;
  background-position: center;
}

.jp-JSONEditor-host.jp-mod-focused {
  background-color: var(--jp-input-active-background);
  border: 1px solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

.jp-Editor.jp-mod-dropTarget {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
.jp-DocumentSearch-input {
  border: none;
  outline: none;
  color: var(--jp-ui-font-color0);
  font-size: var(--jp-ui-font-size1);
  background-color: var(--jp-layout-color0);
  font-family: var(--jp-ui-font-family);
  padding: 2px 1px;
  resize: none;
}

.jp-DocumentSearch-overlay {
  position: absolute;
  background-color: var(--jp-toolbar-background);
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  border-left: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  top: 0;
  right: 0;
  z-index: 7;
  min-width: 405px;
  padding: 2px;
  font-size: var(--jp-ui-font-size1);

  --jp-private-document-search-button-height: 20px;
}

.jp-DocumentSearch-overlay button {
  background-color: var(--jp-toolbar-background);
  outline: 0;
}

.jp-DocumentSearch-overlay button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-overlay button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-overlay-row {
  display: flex;
  align-items: center;
  margin-bottom: 2px;
}

.jp-DocumentSearch-button-content {
  display: inline-block;
  cursor: pointer;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-button-content svg {
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-input-wrapper {
  border: var(--jp-border-width) solid var(--jp-border-color0);
  display: flex;
  background-color: var(--jp-layout-color0);
  margin: 2px;
}

.jp-DocumentSearch-input-wrapper:focus-within {
  border-color: var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper {
  all: initial;
  overflow: hidden;
  display: inline-block;
  border: none;
  box-sizing: border-box;
}

.jp-DocumentSearch-toggle-wrapper {
  width: 14px;
  height: 14px;
}

.jp-DocumentSearch-button-wrapper {
  width: var(--jp-private-document-search-button-height);
  height: var(--jp-private-document-search-button-height);
}

.jp-DocumentSearch-toggle-wrapper:focus,
.jp-DocumentSearch-button-wrapper:focus {
  outline: var(--jp-border-width) solid
    var(--jp-cell-editor-active-border-color);
  outline-offset: -1px;
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper,
.jp-DocumentSearch-button-content:focus {
  outline: none;
}

.jp-DocumentSearch-toggle-placeholder {
  width: 5px;
}

.jp-DocumentSearch-input-button::before {
  display: block;
  padding-top: 100%;
}

.jp-DocumentSearch-input-button-off {
  opacity: var(--jp-search-toggle-off-opacity);
}

.jp-DocumentSearch-input-button-off:hover {
  opacity: var(--jp-search-toggle-hover-opacity);
}

.jp-DocumentSearch-input-button-on {
  opacity: var(--jp-search-toggle-on-opacity);
}

.jp-DocumentSearch-index-counter {
  padding-left: 10px;
  padding-right: 10px;
  user-select: none;
  min-width: 35px;
  display: inline-block;
}

.jp-DocumentSearch-up-down-wrapper {
  display: inline-block;
  padding-right: 2px;
  margin-left: auto;
  white-space: nowrap;
}

.jp-DocumentSearch-spacer {
  margin-left: auto;
}

.jp-DocumentSearch-up-down-wrapper button {
  outline: 0;
  border: none;
  width: var(--jp-private-document-search-button-height);
  height: var(--jp-private-document-search-button-height);
  vertical-align: middle;
  margin: 1px 5px 2px;
}

.jp-DocumentSearch-up-down-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-up-down-button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-filter-button {
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-filter-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-filter-button-enabled {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-filter-button-enabled:hover {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-search-options {
  padding: 0 8px;
  margin-left: 3px;
  width: 100%;
  display: grid;
  justify-content: start;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  justify-items: stretch;
}

.jp-DocumentSearch-search-filter-disabled {
  color: var(--jp-ui-font-color2);
}

.jp-DocumentSearch-search-filter {
  display: flex;
  align-items: center;
  user-select: none;
}

.jp-DocumentSearch-regex-error {
  color: var(--jp-error-color0);
}

.jp-DocumentSearch-replace-button-wrapper {
  overflow: hidden;
  display: inline-block;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color0);
  margin: auto 2px;
  padding: 1px 4px;
  height: calc(var(--jp-private-document-search-button-height) + 2px);
}

.jp-DocumentSearch-replace-button-wrapper:focus {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-replace-button {
  display: inline-block;
  text-align: center;
  cursor: pointer;
  box-sizing: border-box;
  color: var(--jp-ui-font-color1);

  /* height - 2 * (padding of wrapper) */
  line-height: calc(var(--jp-private-document-search-button-height) - 2px);
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-replace-button:focus {
  outline: none;
}

.jp-DocumentSearch-replace-wrapper-class {
  margin-left: 14px;
  display: flex;
}

.jp-DocumentSearch-replace-toggle {
  border: none;
  background-color: var(--jp-toolbar-background);
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-replace-toggle:hover {
  background-color: var(--jp-layout-color2);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.cm-editor {
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  border: 0;
  border-radius: 0;
  height: auto;

  /* Changed to auto to autogrow */
}

.cm-editor pre {
  padding: 0 var(--jp-code-padding);
}

.jp-CodeMirrorEditor[data-type='inline'] .cm-dialog {
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

.jp-CodeMirrorEditor {
  cursor: text;
}

/* When zoomed out 67% and 33% on a screen of 1440 width x 900 height */
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
    border-left: var(--jp-code-cursor-width1) solid
      var(--jp-editor-cursor-color);
  }
}

/* When zoomed out less than 33% */
@media screen and (min-width: 4320px) {
  .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
    border-left: var(--jp-code-cursor-width2) solid
      var(--jp-editor-cursor-color);
  }
}

.cm-editor.jp-mod-readOnly .cm-cursor {
  display: none;
}

.jp-CollaboratorCursor {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: none;
  border-bottom: 3px solid;
  background-clip: content-box;
  margin-left: -5px;
  margin-right: -5px;
}

.cm-searching,
.cm-searching span {
  /* `.cm-searching span`: we need to override syntax highlighting */
  background-color: var(--jp-search-unselected-match-background-color);
  color: var(--jp-search-unselected-match-color);
}

.cm-searching::selection,
.cm-searching span::selection {
  background-color: var(--jp-search-unselected-match-background-color);
  color: var(--jp-search-unselected-match-color);
}

.jp-current-match > .cm-searching,
.jp-current-match > .cm-searching span,
.cm-searching > .jp-current-match,
.cm-searching > .jp-current-match span {
  background-color: var(--jp-search-selected-match-background-color);
  color: var(--jp-search-selected-match-color);
}

.jp-current-match > .cm-searching::selection,
.cm-searching > .jp-current-match::selection,
.jp-current-match > .cm-searching span::selection {
  background-color: var(--jp-search-selected-match-background-color);
  color: var(--jp-search-selected-match-color);
}

.cm-trailingspace {
  background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAFCAYAAAB4ka1VAAAAsElEQVQIHQGlAFr/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7+r3zKmT0/+pk9P/7+r3zAAAAAAAAAAABAAAAAAAAAAA6OPzM+/q9wAAAAAA6OPzMwAAAAAAAAAAAgAAAAAAAAAAGR8NiRQaCgAZIA0AGR8NiQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQyoYJ/SY80UAAAAASUVORK5CYII=);
  background-position: center left;
  background-repeat: repeat-x;
}

.jp-CollaboratorCursor-hover {
  position: absolute;
  z-index: 1;
  transform: translateX(-50%);
  color: white;
  border-radius: 3px;
  padding-left: 4px;
  padding-right: 4px;
  padding-top: 1px;
  padding-bottom: 1px;
  text-align: center;
  font-size: var(--jp-ui-font-size1);
  white-space: nowrap;
}

.jp-CodeMirror-ruler {
  border-left: 1px dashed var(--jp-border-color2);
}

/* Styles for shared cursors (remote cursor locations and selected ranges) */
.jp-CodeMirrorEditor .cm-ySelectionCaret {
  position: relative;
  border-left: 1px solid black;
  margin-left: -1px;
  margin-right: -1px;
  box-sizing: border-box;
}

.jp-CodeMirrorEditor .cm-ySelectionCaret > .cm-ySelectionInfo {
  white-space: nowrap;
  position: absolute;
  top: -1.15em;
  padding-bottom: 0.05em;
  left: -1px;
  font-size: 0.95em;
  font-family: var(--jp-ui-font-family);
  font-weight: bold;
  line-height: normal;
  user-select: none;
  color: white;
  padding-left: 2px;
  padding-right: 2px;
  z-index: 101;
  transition: opacity 0.3s ease-in-out;
}

.jp-CodeMirrorEditor .cm-ySelectionInfo {
  transition-delay: 0.7s;
  opacity: 0;
}

.jp-CodeMirrorEditor .cm-ySelectionCaret:hover > .cm-ySelectionInfo {
  opacity: 1;
  transition-delay: 0s;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MimeDocument {
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-filebrowser-button-height: 28px;
  --jp-private-filebrowser-button-width: 48px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FileBrowser .jp-SidePanel-content {
  display: flex;
  flex-direction: column;
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  flex-wrap: wrap;
  row-gap: 12px;
  border-bottom: none;
  height: auto;
  margin: 8px 12px 0;
  box-shadow: none;
  padding: 0;
  justify-content: flex-start;
}

.jp-FileBrowser-Panel {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
}

.jp-BreadCrumbs {
  flex: 0 0 auto;
  margin: 8px 12px;
}

.jp-BreadCrumbs-item {
  margin: 0 2px;
  padding: 0 2px;
  border-radius: var(--jp-border-radius);
  cursor: pointer;
}

.jp-BreadCrumbs-item:hover {
  background-color: var(--jp-layout-color2);
}

.jp-BreadCrumbs-item:first-child {
  margin-left: 0;
}

.jp-BreadCrumbs-item.jp-mod-dropTarget {
  background-color: var(--jp-brand-color2);
  opacity: 0.7;
}

/*-----------------------------------------------------------------------------
| Buttons
|----------------------------------------------------------------------------*/

.jp-FileBrowser-toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  padding-left: 0;
  padding-right: 2px;
  align-items: center;
  height: unset;
}

.jp-FileBrowser-toolbar > .jp-Toolbar-item .jp-ToolbarButtonComponent {
  width: 40px;
}

/*-----------------------------------------------------------------------------
| Other styles
|----------------------------------------------------------------------------*/

.jp-FileDialog.jp-mod-conflict input {
  color: var(--jp-error-color1);
}

.jp-FileDialog .jp-new-name-title {
  margin-top: 12px;
}

.jp-LastModified-hidden {
  display: none;
}

.jp-FileSize-hidden {
  display: none;
}

.jp-FileBrowser .lm-AccordionPanel > h3:first-child {
  display: none;
}

/*-----------------------------------------------------------------------------
| DirListing
|----------------------------------------------------------------------------*/

.jp-DirListing {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  outline: 0;
}

.jp-DirListing-header {
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  overflow: hidden;
  border-top: var(--jp-border-width) solid var(--jp-border-color2);
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
}

.jp-DirListing-headerItem {
  padding: 4px 12px 2px;
  font-weight: 500;
}

.jp-DirListing-headerItem:hover {
  background: var(--jp-layout-color2);
}

.jp-DirListing-headerItem.jp-id-name {
  flex: 1 0 84px;
}

.jp-DirListing-headerItem.jp-id-modified {
  flex: 0 0 112px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-DirListing-headerItem.jp-id-filesize {
  flex: 0 0 75px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-id-narrow {
  display: none;
  flex: 0 0 5px;
  padding: 4px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
  color: var(--jp-border-color2);
}

.jp-DirListing-narrow .jp-id-narrow {
  display: block;
}

.jp-DirListing-narrow .jp-id-modified,
.jp-DirListing-narrow .jp-DirListing-itemModified {
  display: none;
}

.jp-DirListing-headerItem.jp-mod-selected {
  font-weight: 600;
}

/* increase specificity to override bundled default */
.jp-DirListing-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-content mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.jp-DirListing-content .jp-DirListing-item.jp-mod-selected mark {
  color: var(--jp-ui-inverse-font-color0);
}

/* Style the directory listing content when a user drops a file to upload */
.jp-DirListing.jp-mod-native-drop .jp-DirListing-content {
  outline: 5px dashed rgba(128, 128, 128, 0.5);
  outline-offset: -10px;
  cursor: copy;
}

.jp-DirListing-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 4px 12px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-DirListing-checkboxWrapper {
  /* Increases hit area of checkbox. */
  padding: 4px;
}

.jp-DirListing-header
  .jp-DirListing-checkboxWrapper
  + .jp-DirListing-headerItem {
  padding-left: 4px;
}

.jp-DirListing-content .jp-DirListing-checkboxWrapper {
  position: relative;
  left: -4px;
  margin: -4px 0 -4px -8px;
}

.jp-DirListing-checkboxWrapper.jp-mod-visible {
  visibility: visible;
}

/* For devices that support hovering, hide checkboxes until hovered, selected...
*/
@media (hover: hover) {
  .jp-DirListing-checkboxWrapper {
    visibility: hidden;
  }

  .jp-DirListing-item:hover .jp-DirListing-checkboxWrapper,
  .jp-DirListing-item.jp-mod-selected .jp-DirListing-checkboxWrapper {
    visibility: visible;
  }
}

.jp-DirListing-item[data-is-dot] {
  opacity: 75%;
}

.jp-DirListing-item.jp-mod-selected {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.jp-DirListing-item.jp-mod-dropTarget {
  background: var(--jp-brand-color3);
}

.jp-DirListing-item:hover:not(.jp-mod-selected) {
  background: var(--jp-layout-color2);
}

.jp-DirListing-itemIcon {
  flex: 0 0 20px;
  margin-right: 4px;
}

.jp-DirListing-itemText {
  flex: 1 0 64px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  user-select: none;
}

.jp-DirListing-itemText:focus {
  outline-width: 2px;
  outline-color: var(--jp-inverse-layout-color1);
  outline-style: solid;
  outline-offset: 1px;
}

.jp-DirListing-item.jp-mod-selected .jp-DirListing-itemText:focus {
  outline-color: var(--jp-layout-color1);
}

.jp-DirListing-itemModified {
  flex: 0 0 125px;
  text-align: right;
}

.jp-DirListing-itemFileSize {
  flex: 0 0 90px;
  text-align: right;
}

.jp-DirListing-editor {
  flex: 1 0 64px;
  outline: none;
  border: none;
  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-item.jp-mod-running .jp-DirListing-itemIcon::before {
  color: var(--jp-success-color1);
  content: '\25CF';
  font-size: 8px;
  position: absolute;
  left: -8px;
}

.jp-DirListing-item.jp-mod-running.jp-mod-selected
  .jp-DirListing-itemIcon::before {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-DirListing-item.lm-mod-drag-image,
.jp-DirListing-item.jp-mod-selected.lm-mod-drag-image {
  font-size: var(--jp-ui-font-size1);
  padding-left: 4px;
  margin-left: 4px;
  width: 160px;
  background-color: var(--jp-ui-inverse-font-color2);
  box-shadow: var(--jp-elevation-z2);
  border-radius: 0;
  color: var(--jp-ui-font-color1);
  transform: translateX(-40%) translateY(-58%);
}

.jp-Document {
  min-width: 120px;
  min-height: 120px;
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Main OutputArea
| OutputArea has a list of Outputs
|----------------------------------------------------------------------------*/

.jp-OutputArea {
  overflow-y: auto;
}

.jp-OutputArea-child {
  display: table;
  table-layout: fixed;
  width: 100%;
  overflow: hidden;
}

.jp-OutputPrompt {
  width: var(--jp-cell-prompt-width);
  color: var(--jp-cell-outprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);

  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-OutputArea-prompt {
  display: table-cell;
  vertical-align: top;
}

.jp-OutputArea-output {
  display: table-cell;
  width: 100%;
  height: auto;
  overflow: auto;
  user-select: text;
  -moz-user-select: text;
  -webkit-user-select: text;
  -ms-user-select: text;
}

.jp-OutputArea .jp-RenderedText {
  padding-left: 1ch;
}

/**
 * Prompt overlay.
 */

.jp-OutputArea-promptOverlay {
  position: absolute;
  top: 0;
  width: var(--jp-cell-prompt-width);
  height: 100%;
  opacity: 0.5;
}

.jp-OutputArea-promptOverlay:hover {
  background: var(--jp-layout-color2);
  box-shadow: inset 0 0 1px var(--jp-inverse-layout-color0);
  cursor: zoom-out;
}

.jp-mod-outputsScrolled .jp-OutputArea-promptOverlay:hover {
  cursor: zoom-in;
}

/**
 * Isolated output.
 */
.jp-OutputArea-output.jp-mod-isolated {
  width: 100%;
  display: block;
}

/*
When drag events occur, `lm-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated {
  position: relative;
}

body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/* pre */

.jp-OutputArea-output pre {
  border: none;
  margin: 0;
  padding: 0;
  overflow-x: auto;
  overflow-y: auto;
  word-break: break-all;
  word-wrap: break-word;
  white-space: pre-wrap;
}

/* tables */

.jp-OutputArea-output.jp-RenderedHTMLCommon table {
  margin-left: 0;
  margin-right: 0;
}

/* description lists */

.jp-OutputArea-output dl,
.jp-OutputArea-output dt,
.jp-OutputArea-output dd {
  display: block;
}

.jp-OutputArea-output dl {
  width: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dt {
  font-weight: bold;
  float: left;
  width: 20%;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dd {
  float: left;
  width: 80%;
  padding: 0;
  margin: 0;
}

.jp-TrimmedOutputs pre {
  background: var(--jp-layout-color3);
  font-size: calc(var(--jp-code-font-size) * 1.4);
  text-align: center;
  text-transform: uppercase;
}

/* Hide the gutter in case of
 *  - nested output areas (e.g. in the case of output widgets)
 *  - mirrored output areas
 */
.jp-OutputArea .jp-OutputArea .jp-OutputArea-prompt {
  display: none;
}

/* Hide empty lines in the output area, for instance due to cleared widgets */
.jp-OutputArea-prompt:empty {
  padding: 0;
  border: 0;
}

/*-----------------------------------------------------------------------------
| executeResult is added to any Output-result for the display of the object
| returned by a cell
|----------------------------------------------------------------------------*/

.jp-OutputArea-output.jp-OutputArea-executeResult {
  margin-left: 0;
  width: 100%;
}

/* Text output with the Out[] prompt needs a top padding to match the
 * alignment of the Out[] prompt itself.
 */
.jp-OutputArea-executeResult .jp-RenderedText.jp-OutputArea-output {
  padding-top: var(--jp-code-padding);
  border-top: var(--jp-border-width) solid transparent;
}

/*-----------------------------------------------------------------------------
| The Stdin output
|----------------------------------------------------------------------------*/

.jp-Stdin-prompt {
  color: var(--jp-content-font-color0);
  padding-right: var(--jp-code-padding);
  vertical-align: baseline;
  flex: 0 0 auto;
}

.jp-Stdin-input {
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  color: inherit;
  background-color: inherit;
  width: 42%;
  min-width: 200px;

  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;

  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0 0.25em;
  margin: 0 0.25em;
  flex: 0 0 70%;
}

.jp-Stdin-input::placeholder {
  opacity: 0;
}

.jp-Stdin-input:focus {
  box-shadow: none;
}

.jp-Stdin-input:focus::placeholder {
  opacity: 1;
}

/*-----------------------------------------------------------------------------
| Output Area View
|----------------------------------------------------------------------------*/

.jp-LinkedOutputView .jp-OutputArea {
  height: 100%;
  display: block;
}

.jp-LinkedOutputView .jp-OutputArea-output:only-child {
  height: 100%;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

@media print {
  .jp-OutputArea-child {
    break-inside: avoid-page;
  }
}

/*-----------------------------------------------------------------------------
| Mobile
|----------------------------------------------------------------------------*/
@media only screen and (max-width: 760px) {
  .jp-OutputPrompt {
    display: table-row;
    text-align: left;
  }

  .jp-OutputArea-child .jp-OutputArea-output {
    display: table-row;
    margin-left: var(--jp-notebook-padding);
  }
}

/* Trimmed outputs warning */
.jp-TrimmedOutputs > a {
  margin: 10px;
  text-decoration: none;
  cursor: pointer;
}

.jp-TrimmedOutputs > a:hover {
  text-decoration: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Table of Contents
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toc-active-width: 4px;
}

.jp-TableOfContents {
  display: flex;
  flex-direction: column;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  height: 100%;
}

.jp-TableOfContents-placeholder {
  text-align: center;
}

.jp-TableOfContents-placeholderContent {
  color: var(--jp-content-font-color2);
  padding: 8px;
}

.jp-TableOfContents-placeholderContent > h3 {
  margin-bottom: var(--jp-content-heading-margin-bottom);
}

.jp-TableOfContents .jp-SidePanel-content {
  overflow-y: auto;
}

.jp-TableOfContents-tree {
  margin: 4px;
}

.jp-TableOfContents ol {
  list-style-type: none;
}

/* stylelint-disable-next-line selector-max-type */
.jp-TableOfContents li > ol {
  /* Align left border with triangle icon center */
  padding-left: 11px;
}

.jp-TableOfContents-content {
  /* left margin for the active heading indicator */
  margin: 0 0 0 var(--jp-private-toc-active-width);
  padding: 0;
  background-color: var(--jp-layout-color1);
}

.jp-tocItem {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-tocItem-heading {
  display: flex;
  cursor: pointer;
}

.jp-tocItem-heading:hover {
  background-color: var(--jp-layout-color2);
}

.jp-tocItem-content {
  display: block;
  padding: 4px 0;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow-x: hidden;
}

.jp-tocItem-collapser {
  height: 20px;
  margin: 2px 2px 0;
  padding: 0;
  background: none;
  border: none;
  cursor: pointer;
}

.jp-tocItem-collapser:hover {
  background-color: var(--jp-layout-color3);
}

/* Active heading indicator */

.jp-tocItem-heading::before {
  content: ' ';
  background: transparent;
  width: var(--jp-private-toc-active-width);
  height: 24px;
  position: absolute;
  left: 0;
  border-radius: var(--jp-border-radius);
}

.jp-tocItem-heading.jp-tocItem-active::before {
  background-color: var(--jp-brand-color1);
}

.jp-tocItem-heading:hover.jp-tocItem-active::before {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapser {
  flex: 0 0 var(--jp-cell-collapser-width);
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
  border-radius: var(--jp-border-radius);
  opacity: 1;
}

.jp-Collapser-child {
  display: block;
  width: 100%;
  box-sizing: border-box;

  /* height: 100% doesn't work because the height of its parent is computed from content */
  position: absolute;
  top: 0;
  bottom: 0;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

/*
Hiding collapsers in print mode.

Note: input and output wrappers have "display: block" propery in print mode.
*/

@media print {
  .jp-Collapser {
    display: none;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Header/Footer
|----------------------------------------------------------------------------*/

/* Hidden by zero height by default */
.jp-CellHeader,
.jp-CellFooter {
  height: 0;
  width: 100%;
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Input
|----------------------------------------------------------------------------*/

/* All input areas */
.jp-InputArea {
  display: table;
  table-layout: fixed;
  width: 100%;
  overflow: hidden;
}

.jp-InputArea-editor {
  display: table-cell;
  overflow: hidden;
  vertical-align: top;

  /* This is the non-active, default styling */
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0;
  background: var(--jp-cell-editor-background);
}

.jp-InputPrompt {
  display: table-cell;
  vertical-align: top;
  width: var(--jp-cell-prompt-width);
  color: var(--jp-cell-inprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  opacity: var(--jp-cell-prompt-opacity);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;

  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/*-----------------------------------------------------------------------------
| Mobile
|----------------------------------------------------------------------------*/
@media only screen and (max-width: 760px) {
  .jp-InputArea-editor {
    display: table-row;
    margin-left: var(--jp-notebook-padding);
  }

  .jp-InputPrompt {
    display: table-row;
    text-align: left;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Placeholder {
  display: table;
  table-layout: fixed;
  width: 100%;
}

.jp-Placeholder-prompt {
  display: table-cell;
  box-sizing: border-box;
}

.jp-Placeholder-content {
  display: table-cell;
  padding: 4px 6px;
  border: 1px solid transparent;
  border-radius: 0;
  background: none;
  box-sizing: border-box;
  cursor: pointer;
}

.jp-Placeholder-contentContainer {
  display: flex;
}

.jp-Placeholder-content:hover,
.jp-InputPlaceholder > .jp-Placeholder-content:hover {
  border-color: var(--jp-layout-color3);
}

.jp-Placeholder-content .jp-MoreHorizIcon {
  width: 32px;
  height: 16px;
  border: 1px solid transparent;
  border-radius: var(--jp-border-radius);
}

.jp-Placeholder-content .jp-MoreHorizIcon:hover {
  border: 1px solid var(--jp-border-color1);
  box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.25);
  background-color: var(--jp-layout-color0);
}

.jp-PlaceholderText {
  white-space: nowrap;
  overflow-x: hidden;
  color: var(--jp-inverse-layout-color3);
  font-family: var(--jp-code-font-family);
}

.jp-InputPlaceholder > .jp-Placeholder-content {
  border-color: var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-cell-scrolling-output-offset: 5px;
}

/*-----------------------------------------------------------------------------
| Cell
|----------------------------------------------------------------------------*/

.jp-Cell {
  padding: var(--jp-cell-padding);
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Common input/output
|----------------------------------------------------------------------------*/

.jp-Cell-inputWrapper,
.jp-Cell-outputWrapper {
  display: flex;
  flex-direction: row;
  padding: 0;
  margin: 0;

  /* Added to reveal the box-shadow on the input and output collapsers. */
  overflow: visible;
}

/* Only input/output areas inside cells */
.jp-Cell-inputArea,
.jp-Cell-outputArea {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Collapser
|----------------------------------------------------------------------------*/

/* Make the output collapser disappear when there is not output, but do so
 * in a manner that leaves it in the layout and preserves its width.
 */
.jp-Cell.jp-mod-noOutputs .jp-Cell-outputCollapser {
  border: none !important;
  background: transparent !important;
}

.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputCollapser {
  min-height: var(--jp-cell-collapser-min-height);
}

/*-----------------------------------------------------------------------------
| Output
|----------------------------------------------------------------------------*/

/* Put a space between input and output when there IS output */
.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputWrapper {
  margin-top: 5px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea {
  overflow-y: auto;
  max-height: 24em;
  margin-left: var(--jp-private-cell-scrolling-output-offset);
  resize: vertical;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea[style*='height'] {
  max-height: unset;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea::after {
  content: ' ';
  box-shadow: inset 0 0 6px 2px rgb(0 0 0 / 30%);
  width: 100%;
  height: 100%;
  position: sticky;
  bottom: 0;
  top: 0;
  margin-top: -50%;
  float: left;
  display: block;
  pointer-events: none;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-child {
  padding-top: 6px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  width: calc(
    var(--jp-cell-prompt-width) - var(--jp-private-cell-scrolling-output-offset)
  );
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-promptOverlay {
  left: calc(-1 * var(--jp-private-cell-scrolling-output-offset));
}

/*-----------------------------------------------------------------------------
| CodeCell
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| MarkdownCell
|----------------------------------------------------------------------------*/

.jp-MarkdownOutput {
  display: table-cell;
  width: 100%;
  margin-top: 0;
  margin-bottom: 0;
  padding-left: var(--jp-code-padding);
}

.jp-MarkdownOutput.jp-RenderedHTMLCommon {
  overflow: auto;
}

/* collapseHeadingButton (show always if hiddenCellsButton is _not_ shown) */
.jp-collapseHeadingButton {
  display: flex;
  min-height: var(--jp-cell-collapser-min-height);
  font-size: var(--jp-code-font-size);
  position: absolute;
  background-color: transparent;
  background-size: 25px;
  background-repeat: no-repeat;
  background-position-x: center;
  background-position-y: top;
  background-image: var(--jp-icon-caret-down);
  right: 0;
  top: 0;
  bottom: 0;
}

.jp-collapseHeadingButton.jp-mod-collapsed {
  background-image: var(--jp-icon-caret-right);
}

/*
 set the container font size to match that of content
 so that the nested collapse buttons have the right size
*/
.jp-MarkdownCell .jp-InputPrompt {
  font-size: var(--jp-content-font-size1);
}

/*
  Align collapseHeadingButton with cell top header
  The font sizes are identical to the ones in packages/rendermime/style/base.css
*/
.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='1'] {
  font-size: var(--jp-content-font-size5);
  background-position-y: calc(0.3 * var(--jp-content-font-size5));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='2'] {
  font-size: var(--jp-content-font-size4);
  background-position-y: calc(0.3 * var(--jp-content-font-size4));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='3'] {
  font-size: var(--jp-content-font-size3);
  background-position-y: calc(0.3 * var(--jp-content-font-size3));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='4'] {
  font-size: var(--jp-content-font-size2);
  background-position-y: calc(0.3 * var(--jp-content-font-size2));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='5'] {
  font-size: var(--jp-content-font-size1);
  background-position-y: top;
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='6'] {
  font-size: var(--jp-content-font-size0);
  background-position-y: top;
}

/* collapseHeadingButton (show only on (hover,active) if hiddenCellsButton is shown) */
.jp-Notebook.jp-mod-showHiddenCellsButton .jp-collapseHeadingButton {
  display: none;
}

.jp-Notebook.jp-mod-showHiddenCellsButton
  :is(.jp-MarkdownCell:hover, .jp-mod-active)
  .jp-collapseHeadingButton {
  display: flex;
}

/* showHiddenCellsButton (only show if jp-mod-showHiddenCellsButton is set, which
is a consequence of the showHiddenCellsButton option in Notebook Settings)*/
.jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton {
  margin-left: calc(var(--jp-cell-prompt-width) + 2 * var(--jp-code-padding));
  margin-top: var(--jp-code-padding);
  border: 1px solid var(--jp-border-color2);
  background-color: var(--jp-border-color3) !important;
  color: var(--jp-content-font-color0) !important;
  display: flex;
}

.jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton:hover {
  background-color: var(--jp-border-color2) !important;
}

.jp-showHiddenCellsButton {
  display: none;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

/*
Using block instead of flex to allow the use of the break-inside CSS property for
cell outputs.
*/

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-notebook-toolbar-padding: 2px 5px 2px 2px;
}

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-NotebookPanel-toolbar {
  padding: var(--jp-notebook-toolbar-padding);

  /* disable paint containment from lumino 2.0 default strict CSS containment */
  contain: style size !important;
}

.jp-Toolbar-item.jp-Notebook-toolbarCellType .jp-select-wrapper.jp-mod-focused {
  border: none;
  box-shadow: none;
}

.jp-Notebook-toolbarCellTypeDropdown select {
  height: 24px;
  font-size: var(--jp-ui-font-size1);
  line-height: 14px;
  border-radius: 0;
  display: block;
}

.jp-Notebook-toolbarCellTypeDropdown span {
  top: 5px !important;
}

.jp-Toolbar-responsive-popup {
  position: absolute;
  height: fit-content;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-end;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: var(--jp-notebook-toolbar-padding);
  z-index: 1;
  right: 0;
  top: 0;
}

.jp-Toolbar > .jp-Toolbar-responsive-opener {
  margin-left: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-Notebook-ExecutionIndicator {
  position: relative;
  display: inline-block;
  height: 100%;
  z-index: 9997;
}

.jp-Notebook-ExecutionIndicator-tooltip {
  visibility: hidden;
  height: auto;
  width: max-content;
  width: -moz-max-content;
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color1);
  text-align: justify;
  border-radius: 6px;
  padding: 0 5px;
  position: fixed;
  display: table;
}

.jp-Notebook-ExecutionIndicator-tooltip.up {
  transform: translateX(-50%) translateY(-100%) translateY(-32px);
}

.jp-Notebook-ExecutionIndicator-tooltip.down {
  transform: translateX(calc(-100% + 16px)) translateY(5px);
}

.jp-Notebook-ExecutionIndicator-tooltip.hidden {
  display: none;
}

.jp-Notebook-ExecutionIndicator:hover .jp-Notebook-ExecutionIndicator-tooltip {
  visibility: visible;
}

.jp-Notebook-ExecutionIndicator span {
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  color: var(--jp-ui-font-color1);
  line-height: 24px;
  display: block;
}

.jp-Notebook-ExecutionIndicator-progress-bar {
  display: flex;
  justify-content: center;
  height: 100%;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*
 * Execution indicator
 */
.jp-tocItem-content::after {
  content: '';

  /* Must be identical to form a circle */
  width: 12px;
  height: 12px;
  background: none;
  border: none;
  position: absolute;
  right: 0;
}

.jp-tocItem-content[data-running='0']::after {
  border-radius: 50%;
  border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
  background: none;
}

.jp-tocItem-content[data-running='1']::after {
  border-radius: 50%;
  border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
  background-color: var(--jp-inverse-layout-color3);
}

.jp-tocItem-content[data-running='0'],
.jp-tocItem-content[data-running='1'] {
  margin-right: 12px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-Notebook-footer {
  height: 27px;
  margin-left: calc(
    var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
      var(--jp-cell-padding)
  );
  width: calc(
    100% -
      (
        var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
          var(--jp-cell-padding) + var(--jp-cell-padding)
      )
  );
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  color: var(--jp-ui-font-color3);
  margin-top: 6px;
  background: none;
  cursor: pointer;
}

.jp-Notebook-footer:focus {
  border-color: var(--jp-cell-editor-active-border-color);
}

/* For devices that support hovering, hide footer until hover */
@media (hover: hover) {
  .jp-Notebook-footer {
    opacity: 0;
  }

  .jp-Notebook-footer:focus,
  .jp-Notebook-footer:hover {
    opacity: 1;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Imports
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-side-by-side-output-size: 1fr;
  --jp-side-by-side-resized-cell: var(--jp-side-by-side-output-size);
  --jp-private-notebook-dragImage-width: 304px;
  --jp-private-notebook-dragImage-height: 36px;
  --jp-private-notebook-selected-color: var(--md-blue-400);
  --jp-private-notebook-active-color: var(--md-green-400);
}

/*-----------------------------------------------------------------------------
| Notebook
|----------------------------------------------------------------------------*/

/* stylelint-disable selector-max-class */

.jp-NotebookPanel {
  display: block;
  height: 100%;
}

.jp-NotebookPanel.jp-Document {
  min-width: 240px;
  min-height: 120px;
}

.jp-Notebook {
  padding: var(--jp-notebook-padding);
  outline: none;
  overflow: auto;
  background: var(--jp-layout-color0);
}

.jp-Notebook.jp-mod-scrollPastEnd::after {
  display: block;
  content: '';
  min-height: var(--jp-notebook-scroll-padding);
}

.jp-MainAreaWidget-ContainStrict .jp-Notebook * {
  contain: strict;
}

.jp-Notebook .jp-Cell {
  overflow: visible;
}

.jp-Notebook .jp-Cell .jp-InputPrompt {
  cursor: move;
}

/*-----------------------------------------------------------------------------
| Notebook state related styling
|
| The notebook and cells each have states, here are the possibilities:
|
| - Notebook
|   - Command
|   - Edit
| - Cell
|   - None
|   - Active (only one can be active)
|   - Selected (the cells actions are applied to)
|   - Multiselected (when multiple selected, the cursor)
|   - No outputs
|----------------------------------------------------------------------------*/

/* Command or edit modes */

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

/* cell is active */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser {
  background: var(--jp-brand-color1);
}

/* cell is dirty */
.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt {
  color: var(--jp-warn-color1);
}

.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt::before {
  color: var(--jp-warn-color1);
  content: '•';
}

.jp-Notebook .jp-Cell.jp-mod-active.jp-mod-dirty .jp-Collapser {
  background: var(--jp-warn-color1);
}

/* collapser is hovered */
.jp-Notebook .jp-Cell .jp-Collapser:hover {
  box-shadow: var(--jp-elevation-z2);
  background: var(--jp-brand-color1);
  opacity: var(--jp-cell-collapser-not-active-hover-opacity);
}

/* cell is active and collapser is hovered */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser:hover {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/* Command mode */

.jp-Notebook.jp-mod-commandMode .jp-Cell.jp-mod-selected {
  background: var(--jp-notebook-multiselected-color);
}

.jp-Notebook.jp-mod-commandMode
  .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {
  background: transparent;
}

/* Edit mode */

.jp-Notebook.jp-mod-editMode .jp-Cell.jp-mod-active .jp-InputArea-editor {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-cell-editor-active-background);
}

/*-----------------------------------------------------------------------------
| Notebook drag and drop
|----------------------------------------------------------------------------*/

.jp-Notebook-cell.jp-mod-dropSource {
  opacity: 0.5;
}

.jp-Notebook-cell.jp-mod-dropTarget,
.jp-Notebook.jp-mod-commandMode
  .jp-Notebook-cell.jp-mod-active.jp-mod-selected.jp-mod-dropTarget {
  border-top-color: var(--jp-private-notebook-selected-color);
  border-top-style: solid;
  border-top-width: 2px;
}

.jp-dragImage {
  display: block;
  flex-direction: row;
  width: var(--jp-private-notebook-dragImage-width);
  height: var(--jp-private-notebook-dragImage-height);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
  overflow: visible;
}

.jp-dragImage-singlePrompt {
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
}

.jp-dragImage .jp-dragImage-content {
  flex: 1 1 auto;
  z-index: 2;
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  line-height: var(--jp-code-line-height);
  padding: var(--jp-code-padding);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background-color);
  color: var(--jp-content-font-color3);
  text-align: left;
  margin: 4px 4px 4px 0;
}

.jp-dragImage .jp-dragImage-prompt {
  flex: 0 0 auto;
  min-width: 36px;
  color: var(--jp-cell-inprompt-font-color);
  padding: var(--jp-code-padding);
  padding-left: 12px;
  font-family: var(--jp-cell-prompt-font-family);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: 1.9;
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
}

.jp-dragImage-multipleBack {
  z-index: -1;
  position: absolute;
  height: 32px;
  width: 300px;
  top: 8px;
  left: 8px;
  background: var(--jp-layout-color2);
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
}

/*-----------------------------------------------------------------------------
| Cell toolbar
|----------------------------------------------------------------------------*/

.jp-NotebookTools {
  display: block;
  min-width: var(--jp-sidebar-min-width);
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);

  /* This is needed so that all font sizing of children done in ems is
    * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  overflow: auto;
}

.jp-ActiveCellTool {
  padding: 12px 0;
  display: flex;
}

.jp-ActiveCellTool-Content {
  flex: 1 1 auto;
}

.jp-ActiveCellTool .jp-ActiveCellTool-CellContent {
  background: var(--jp-cell-editor-background);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0;
  min-height: 29px;
}

.jp-ActiveCellTool .jp-InputPrompt {
  min-width: calc(var(--jp-cell-prompt-width) * 0.75);
}

.jp-ActiveCellTool-CellContent > pre {
  padding: 5px 4px;
  margin: 0;
  white-space: normal;
}

.jp-MetadataEditorTool {
  flex-direction: column;
  padding: 12px 0;
}

.jp-RankedPanel > :not(:first-child) {
  margin-top: 12px;
}

.jp-KeySelector select.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: var(--jp-border-width) solid var(--jp-border-color1);
}

.jp-KeySelector label,
.jp-MetadataEditorTool label,
.jp-NumberSetter label {
  line-height: 1.4;
}

.jp-NotebookTools .jp-select-wrapper {
  margin-top: 4px;
  margin-bottom: 0;
}

.jp-NumberSetter input {
  width: 100%;
  margin-top: 4px;
}

.jp-NotebookTools .jp-Collapse {
  margin-top: 16px;
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-Notebook {
  --jp-content-font-size1: var(--jp-content-presentation-font-size1);
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}

.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-InputPrompt,
.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-OutputPrompt {
  flex: 0 0 110px;
}

/*-----------------------------------------------------------------------------
| Side-by-side Mode (.jp-mod-sideBySide)
|----------------------------------------------------------------------------*/
.jp-mod-sideBySide.jp-Notebook .jp-Notebook-cell {
  margin-top: 3em;
  margin-bottom: 3em;
  margin-left: 5%;
  margin-right: 5%;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell {
  display: grid;
  grid-template-columns: minmax(0, 1fr) min-content minmax(
      0,
      var(--jp-side-by-side-output-size)
    );
  grid-template-rows: auto minmax(0, 1fr) auto;
  grid-template-areas:
    'header header header'
    'input handle output'
    'footer footer footer';
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell.jp-mod-resizedCell {
  grid-template-columns: minmax(0, 1fr) min-content minmax(
      0,
      var(--jp-side-by-side-resized-cell)
    );
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellHeader {
  grid-area: header;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-inputWrapper {
  grid-area: input;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-outputWrapper {
  /* overwrite the default margin (no vertical separation needed in side by side move */
  margin-top: 0;
  grid-area: output;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellFooter {
  grid-area: footer;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle {
  grid-area: handle;
  user-select: none;
  display: block;
  height: 100%;
  cursor: ew-resize;
  padding: 0 var(--jp-cell-padding);
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle::after {
  content: '';
  display: block;
  background: var(--jp-border-color2);
  height: 100%;
  width: 5px;
}

.jp-mod-sideBySide.jp-Notebook
  .jp-CodeCell.jp-mod-resizedCell
  .jp-CellResizeHandle::after {
  background: var(--jp-border-color0);
}

.jp-CellResizeHandle {
  display: none;
}

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Cell-Placeholder {
  padding-left: 55px;
}

.jp-Cell-Placeholder-wrapper {
  background: #fff;
  border: 1px solid;
  border-color: #e5e6e9 #dfe0e4 #d0d1d5;
  border-radius: 4px;
  -webkit-border-radius: 4px;
  margin: 10px 15px;
}

.jp-Cell-Placeholder-wrapper-inner {
  padding: 15px;
  position: relative;
}

.jp-Cell-Placeholder-wrapper-body {
  background-repeat: repeat;
  background-size: 50% auto;
}

.jp-Cell-Placeholder-wrapper-body div {
  background: #f6f7f8;
  background-image: -webkit-linear-gradient(
    left,
    #f6f7f8 0%,
    #edeef1 20%,
    #f6f7f8 40%,
    #f6f7f8 100%
  );
  background-repeat: no-repeat;
  background-size: 800px 104px;
  height: 104px;
  position: absolute;
  right: 15px;
  left: 15px;
  top: 15px;
}

div.jp-Cell-Placeholder-h1 {
  top: 20px;
  height: 20px;
  left: 15px;
  width: 150px;
}

div.jp-Cell-Placeholder-h2 {
  left: 15px;
  top: 50px;
  height: 10px;
  width: 100px;
}

div.jp-Cell-Placeholder-content-1,
div.jp-Cell-Placeholder-content-2,
div.jp-Cell-Placeholder-content-3 {
  left: 15px;
  right: 15px;
  height: 10px;
}

div.jp-Cell-Placeholder-content-1 {
  top: 100px;
}

div.jp-Cell-Placeholder-content-2 {
  top: 120px;
}

div.jp-Cell-Placeholder-content-3 {
  top: 140px;
}

</style>
<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/

:root {
  /* Elevation
   *
   * We style box-shadows using Material Design's idea of elevation. These particular numbers are taken from here:
   *
   * https://github.com/material-components/material-components-web
   * https://material-components-web.appspot.com/elevation.html
   */

  --jp-shadow-base-lightness: 0;
  --jp-shadow-umbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.2
  );
  --jp-shadow-penumbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.14
  );
  --jp-shadow-ambient-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.12
  );
  --jp-elevation-z0: none;
  --jp-elevation-z1: 0 2px 1px -1px var(--jp-shadow-umbra-color),
    0 1px 1px 0 var(--jp-shadow-penumbra-color),
    0 1px 3px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z2: 0 3px 1px -2px var(--jp-shadow-umbra-color),
    0 2px 2px 0 var(--jp-shadow-penumbra-color),
    0 1px 5px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z4: 0 2px 4px -1px var(--jp-shadow-umbra-color),
    0 4px 5px 0 var(--jp-shadow-penumbra-color),
    0 1px 10px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z6: 0 3px 5px -1px var(--jp-shadow-umbra-color),
    0 6px 10px 0 var(--jp-shadow-penumbra-color),
    0 1px 18px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z8: 0 5px 5px -3px var(--jp-shadow-umbra-color),
    0 8px 10px 1px var(--jp-shadow-penumbra-color),
    0 3px 14px 2px var(--jp-shadow-ambient-color);
  --jp-elevation-z12: 0 7px 8px -4px var(--jp-shadow-umbra-color),
    0 12px 17px 2px var(--jp-shadow-penumbra-color),
    0 5px 22px 4px var(--jp-shadow-ambient-color);
  --jp-elevation-z16: 0 8px 10px -5px var(--jp-shadow-umbra-color),
    0 16px 24px 2px var(--jp-shadow-penumbra-color),
    0 6px 30px 5px var(--jp-shadow-ambient-color);
  --jp-elevation-z20: 0 10px 13px -6px var(--jp-shadow-umbra-color),
    0 20px 31px 3px var(--jp-shadow-penumbra-color),
    0 8px 38px 7px var(--jp-shadow-ambient-color);
  --jp-elevation-z24: 0 11px 15px -7px var(--jp-shadow-umbra-color),
    0 24px 38px 3px var(--jp-shadow-penumbra-color),
    0 9px 46px 8px var(--jp-shadow-ambient-color);

  /* Borders
   *
   * The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-400);
  --jp-border-color1: var(--md-grey-400);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-200);
  --jp-inverse-border-color: var(--md-grey-600);
  --jp-border-radius: 2px;

  /* UI Fonts
   *
   * The UI font CSS variables are used for the typography all of the JupyterLab
   * user interface elements that are not directly user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-ui-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: 0.83333em;
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: 1.2em;
  --jp-ui-font-size3: 1.44em;
  --jp-ui-font-family: system-ui, -apple-system, blinkmacsystemfont, 'Segoe UI',
    helvetica, arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
    'Segoe UI Symbol';

  /*
   * Use these font colors against the corresponding main layout colors.
   * In a light theme, these go from dark to light.
   */

  /* Defaults use Material Design specification */
  --jp-ui-font-color0: rgba(0, 0, 0, 1);
  --jp-ui-font-color1: rgba(0, 0, 0, 0.87);
  --jp-ui-font-color2: rgba(0, 0, 0, 0.54);
  --jp-ui-font-color3: rgba(0, 0, 0, 0.38);

  /*
   * Use these against the brand/accent/warn/error colors.
   * These will typically go from light to darker, in both a dark and light theme.
   */

  --jp-ui-inverse-font-color0: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color1: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color2: rgba(255, 255, 255, 0.7);
  --jp-ui-inverse-font-color3: rgba(255, 255, 255, 0.5);

  /* Content Fonts
   *
   * Content font variables are used for typography of user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-content-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-content-line-height: 1.6;
  --jp-content-font-scale-factor: 1.2;
  --jp-content-font-size0: 0.83333em;
  --jp-content-font-size1: 14px; /* Base font size */
  --jp-content-font-size2: 1.2em;
  --jp-content-font-size3: 1.44em;
  --jp-content-font-size4: 1.728em;
  --jp-content-font-size5: 2.0736em;

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-content-presentation-font-size1: 17px;
  --jp-content-heading-line-height: 1;
  --jp-content-heading-margin-top: 1.2em;
  --jp-content-heading-margin-bottom: 0.8em;
  --jp-content-heading-font-weight: 500;

  /* Defaults use Material Design specification */
  --jp-content-font-color0: rgba(0, 0, 0, 1);
  --jp-content-font-color1: rgba(0, 0, 0, 0.87);
  --jp-content-font-color2: rgba(0, 0, 0, 0.54);
  --jp-content-font-color3: rgba(0, 0, 0, 0.38);
  --jp-content-link-color: var(--md-blue-900);
  --jp-content-font-family: system-ui, -apple-system, blinkmacsystemfont,
    'Segoe UI', helvetica, arial, sans-serif, 'Apple Color Emoji',
    'Segoe UI Emoji', 'Segoe UI Symbol';

  /*
   * Code Fonts
   *
   * Code font variables are used for typography of code and other monospaces content.
   */

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.3077; /* 17px for 13px base */
  --jp-code-padding: 5px; /* 5px for 13px base, codemirror highlighting needs integer px value */
  --jp-code-font-family-default: menlo, consolas, 'DejaVu Sans Mono', monospace;
  --jp-code-font-family: var(--jp-code-font-family-default);

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-code-presentation-font-size: 16px;

  /* may need to tweak cursor width if you change font size */
  --jp-code-cursor-width0: 1.4px;
  --jp-code-cursor-width1: 2px;
  --jp-code-cursor-width2: 4px;

  /* Layout
   *
   * The following are the main layout colors use in JupyterLab. In a light
   * theme these would go from light to dark.
   */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);
  --jp-layout-color4: var(--md-grey-600);

  /* Inverse Layout
   *
   * The following are the inverse layout colors use in JupyterLab. In a light
   * theme these would go from dark to light.
   */

  --jp-inverse-layout-color0: #111;
  --jp-inverse-layout-color1: var(--md-grey-900);
  --jp-inverse-layout-color2: var(--md-grey-800);
  --jp-inverse-layout-color3: var(--md-grey-700);
  --jp-inverse-layout-color4: var(--md-grey-600);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-900);
  --jp-brand-color1: var(--md-blue-700);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);
  --jp-brand-color4: var(--md-blue-50);
  --jp-accent-color0: var(--md-green-900);
  --jp-accent-color1: var(--md-green-700);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-900);
  --jp-warn-color1: var(--md-orange-700);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);
  --jp-error-color0: var(--md-red-900);
  --jp-error-color1: var(--md-red-700);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);
  --jp-success-color0: var(--md-green-900);
  --jp-success-color1: var(--md-green-700);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);
  --jp-info-color0: var(--md-cyan-900);
  --jp-info-color1: var(--md-cyan-700);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;
  --jp-cell-collapser-width: 8px;
  --jp-cell-collapser-min-height: 20px;
  --jp-cell-collapser-not-active-hover-opacity: 0.6;
  --jp-cell-editor-background: var(--md-grey-100);
  --jp-cell-editor-border-color: var(--md-grey-300);
  --jp-cell-editor-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-cell-editor-active-background: var(--jp-layout-color0);
  --jp-cell-editor-active-border-color: var(--jp-brand-color1);
  --jp-cell-prompt-width: 64px;
  --jp-cell-prompt-font-family: var(--jp-code-font-family-default);
  --jp-cell-prompt-letter-spacing: 0;
  --jp-cell-prompt-opacity: 1;
  --jp-cell-prompt-not-active-opacity: 0.5;
  --jp-cell-prompt-not-active-font-color: var(--md-grey-700);

  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307fc1;

  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #bf5b3d;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-select-background: var(--jp-layout-color1);
  --jp-notebook-multiselected-color: var(--md-blue-50);

  /* The scroll padding is calculated to fill enough space at the bottom of the
  notebook to show one single-line cell (with appropriate padding) at the top
  when the notebook is scrolled all the way to the bottom. We also subtract one
  pixel so that no scrollbar appears if we have just one single-line cell in the
  notebook. This padding is to enable a 'scroll past end' feature in a notebook.
  */
  --jp-notebook-scroll-padding: calc(
    100% - var(--jp-code-font-size) * var(--jp-code-line-height) -
      var(--jp-code-padding) - var(--jp-cell-padding) - 1px
  );

  /* Rendermime styles */

  --jp-rendermime-error-background: #fdd;
  --jp-rendermime-table-row-background: var(--md-grey-100);
  --jp-rendermime-table-row-hover-background: var(--md-light-blue-50);

  /* Dialog specific styles */

  --jp-dialog-background: rgba(0, 0, 0, 0.25);

  /* Console specific styles */

  --jp-console-padding: 10px;

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--jp-border-color1);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color1);
  --jp-toolbar-box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.24);
  --jp-toolbar-header-margin: 4px 4px 0 4px;
  --jp-toolbar-active-background: var(--md-grey-300);

  /* Statusbar specific styles */

  --jp-statusbar-height: 24px;

  /* Input field styles */

  --jp-input-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-input-active-background: var(--jp-layout-color1);
  --jp-input-hover-background: var(--jp-layout-color1);
  --jp-input-background: var(--md-grey-100);
  --jp-input-border-color: var(--jp-inverse-border-color);
  --jp-input-active-border-color: var(--jp-brand-color1);
  --jp-input-active-box-shadow-color: rgba(19, 124, 189, 0.3);

  /* General editor styles */

  --jp-editor-selected-background: #d9d9d9;
  --jp-editor-selected-focused-background: #d7d4f0;
  --jp-editor-cursor-color: var(--jp-ui-font-color0);

  /* Code mirror specific styles */

  --jp-mirror-editor-keyword-color: #008000;
  --jp-mirror-editor-atom-color: #88f;
  --jp-mirror-editor-number-color: #080;
  --jp-mirror-editor-def-color: #00f;
  --jp-mirror-editor-variable-color: var(--md-grey-900);
  --jp-mirror-editor-variable-2-color: rgb(0, 54, 109);
  --jp-mirror-editor-variable-3-color: #085;
  --jp-mirror-editor-punctuation-color: #05a;
  --jp-mirror-editor-property-color: #05a;
  --jp-mirror-editor-operator-color: #a2f;
  --jp-mirror-editor-comment-color: #408080;
  --jp-mirror-editor-string-color: #ba2121;
  --jp-mirror-editor-string-2-color: #708;
  --jp-mirror-editor-meta-color: #a2f;
  --jp-mirror-editor-qualifier-color: #555;
  --jp-mirror-editor-builtin-color: #008000;
  --jp-mirror-editor-bracket-color: #997;
  --jp-mirror-editor-tag-color: #170;
  --jp-mirror-editor-attribute-color: #00c;
  --jp-mirror-editor-header-color: blue;
  --jp-mirror-editor-quote-color: #090;
  --jp-mirror-editor-link-color: #00c;
  --jp-mirror-editor-error-color: #f00;
  --jp-mirror-editor-hr-color: #999;

  /*
    RTC user specific colors.
    These colors are used for the cursor, username in the editor,
    and the icon of the user.
  */

  --jp-collaborator-color1: #ffad8e;
  --jp-collaborator-color2: #dac83d;
  --jp-collaborator-color3: #72dd76;
  --jp-collaborator-color4: #00e4d0;
  --jp-collaborator-color5: #45d4ff;
  --jp-collaborator-color6: #e2b1ff;
  --jp-collaborator-color7: #ff9de6;

  /* Vega extension styles */

  --jp-vega-background: white;

  /* Sidebar-related styles */

  --jp-sidebar-min-width: 250px;

  /* Search-related styles */

  --jp-search-toggle-off-opacity: 0.5;
  --jp-search-toggle-hover-opacity: 0.8;
  --jp-search-toggle-on-opacity: 1;
  --jp-search-selected-match-background-color: rgb(245, 200, 0);
  --jp-search-selected-match-color: black;
  --jp-search-unselected-match-background-color: var(
    --jp-inverse-layout-color0
  );
  --jp-search-unselected-match-color: var(--jp-ui-inverse-font-color0);

  /* Icon colors that work well with light or dark backgrounds */
  --jp-icon-contrast-color0: var(--md-purple-600);
  --jp-icon-contrast-color1: var(--md-green-600);
  --jp-icon-contrast-color2: var(--md-pink-600);
  --jp-icon-contrast-color3: var(--md-blue-600);

  /* Button colors */
  --jp-accept-color-normal: var(--md-blue-700);
  --jp-accept-color-hover: var(--md-blue-800);
  --jp-accept-color-active: var(--md-blue-900);
  --jp-warn-color-normal: var(--md-red-700);
  --jp-warn-color-hover: var(--md-red-800);
  --jp-warn-color-active: var(--md-red-900);
  --jp-reject-color-normal: var(--md-grey-600);
  --jp-reject-color-hover: var(--md-grey-700);
  --jp-reject-color-active: var(--md-grey-800);

  /* File or activity icons and switch semantic variables */
  --jp-jupyter-icon-color: #f37626;
  --jp-notebook-icon-color: #f37626;
  --jp-json-icon-color: var(--md-orange-700);
  --jp-console-icon-background-color: var(--md-blue-700);
  --jp-console-icon-color: white;
  --jp-terminal-icon-background-color: var(--md-grey-800);
  --jp-terminal-icon-color: var(--md-grey-200);
  --jp-text-editor-icon-color: var(--md-grey-700);
  --jp-inspector-icon-color: var(--md-grey-700);
  --jp-switch-color: var(--md-grey-400);
  --jp-switch-true-position-color: var(--md-orange-900);
}
</style>
<style type="text/css">
/* Force rendering true colors when outputing to pdf */
* {
  -webkit-print-color-adjust: exact;
}

/* Misc */
a.anchor-link {
  display: none;
}

/* Input area styling */
.jp-InputArea {
  overflow: hidden;
}

.jp-InputArea-editor {
  overflow: hidden;
}

.cm-editor.cm-s-jupyter .highlight pre {
/* weird, but --jp-code-padding defined to be 5px but 4px horizontal padding is hardcoded for pre.cm-line */
  padding: var(--jp-code-padding) 4px;
  margin: 0;

  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
  color: inherit;

}

.jp-OutputArea-output pre {
  line-height: inherit;
  font-family: inherit;
}

.jp-RenderedText pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
}

/* Hiding the collapser by default */
.jp-Collapser {
  display: none;
}

@page {
    margin: 0.5in; /* Margin for each printed piece of paper */
}

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }
}
</style>
<!-- Load mathjax -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"> </script>
<!-- MathJax configuration -->
<script type="text/x-mathjax-config">
    init_mathjax = function() {
        if (window.MathJax) {
        // MathJax loaded
            MathJax.Hub.Config({
                TeX: {
                    equationNumbers: {
                    autoNumber: "AMS",
                    useLabelIds: true
                    }
                },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                    processEscapes: true,
                    processEnvironments: true
                },
                displayAlign: 'center',
                messageStyle: 'none',
                CommonHTML: {
                    linebreaks: {
                    automatic: true
                    }
                }
            });

            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        }
    }
    init_mathjax();
    </script>
<!-- End of mathjax configuration --><script type="module">
  document.addEventListener("DOMContentLoaded", async () => {
    const diagrams = document.querySelectorAll(".jp-Mermaid > pre.mermaid");
    // do not load mermaidjs if not needed
    if (!diagrams.length) {
      return;
    }
    const mermaid = (await import("https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.7.0/mermaid.esm.min.mjs")).default;
    const parser = new DOMParser();

    mermaid.initialize({
      maxTextSize: 100000,
      maxEdges: 100000,
      startOnLoad: false,
      fontFamily: window
        .getComputedStyle(document.body)
        .getPropertyValue("--jp-ui-font-family"),
      theme: document.querySelector("body[data-jp-theme-light='true']")
        ? "default"
        : "dark",
    });

    let _nextMermaidId = 0;

    function makeMermaidImage(svg) {
      const img = document.createElement("img");
      const doc = parser.parseFromString(svg, "image/svg+xml");
      const svgEl = doc.querySelector("svg");
      const { maxWidth } = svgEl?.style || {};
      const firstTitle = doc.querySelector("title");
      const firstDesc = doc.querySelector("desc");

      img.setAttribute("src", `data:image/svg+xml,${encodeURIComponent(svg)}`);
      if (maxWidth) {
        img.width = parseInt(maxWidth);
      }
      if (firstTitle) {
        img.setAttribute("alt", firstTitle.textContent);
      }
      if (firstDesc) {
        const caption = document.createElement("figcaption");
        caption.className = "sr-only";
        caption.textContent = firstDesc.textContent;
        return [img, caption];
      }
      return [img];
    }

    async function makeMermaidError(text) {
      let errorMessage = "";
      try {
        await mermaid.parse(text);
      } catch (err) {
        errorMessage = `${err}`;
      }

      const result = document.createElement("details");
      result.className = 'jp-RenderedMermaid-Details';
      const summary = document.createElement("summary");
      summary.className = 'jp-RenderedMermaid-Summary';
      const pre = document.createElement("pre");
      const code = document.createElement("code");
      code.innerText = text;
      pre.appendChild(code);
      summary.appendChild(pre);
      result.appendChild(summary);

      const warning = document.createElement("pre");
      warning.innerText = errorMessage;
      result.appendChild(warning);
      return [result];
    }

    async function renderOneMarmaid(src) {
      const id = `jp-mermaid-${_nextMermaidId++}`;
      const parent = src.parentNode;
      let raw = src.textContent.trim();
      const el = document.createElement("div");
      el.style.visibility = "hidden";
      document.body.appendChild(el);
      let results = null;
      let output = null;
      try {
        let { svg } = await mermaid.render(id, raw, el);
        svg = cleanMermaidSvg(svg);
        results = makeMermaidImage(svg);
        output = document.createElement("figure");
        results.map(output.appendChild, output);
      } catch (err) {
        parent.classList.add("jp-mod-warning");
        results = await makeMermaidError(raw);
        output = results[0];
      } finally {
        el.remove();
      }
      parent.classList.add("jp-RenderedMermaid");
      parent.appendChild(output);
    }


    /**
     * Post-process to ensure mermaid diagrams contain only valid SVG and XHTML.
     */
    function cleanMermaidSvg(svg) {
      return svg.replace(RE_VOID_ELEMENT, replaceVoidElement);
    }


    /**
     * A regular expression for all void elements, which may include attributes and
     * a slash.
     *
     * @see https://developer.mozilla.org/en-US/docs/Glossary/Void_element
     *
     * Of these, only `<br>` is generated by Mermaid in place of `\n`,
     * but _any_ "malformed" tag will break the SVG rendering entirely.
     */
    const RE_VOID_ELEMENT =
      /<\s*(area|base|br|col|embed|hr|img|input|link|meta|param|source|track|wbr)\s*([^>]*?)\s*>/gi;

    /**
     * Ensure a void element is closed with a slash, preserving any attributes.
     */
    function replaceVoidElement(match, tag, rest) {
      rest = rest.trim();
      if (!rest.endsWith('/')) {
        rest = `${rest} /`;
      }
      return `<${tag} ${rest}>`;
    }

    void Promise.all([...diagrams].map(renderOneMarmaid));
  });
</script>
<style>
  .jp-Mermaid:not(.jp-RenderedMermaid) {
    display: none;
  }

  .jp-RenderedMermaid {
    overflow: auto;
    display: flex;
  }

  .jp-RenderedMermaid.jp-mod-warning {
    width: auto;
    padding: 0.5em;
    margin-top: 0.5em;
    border: var(--jp-border-width) solid var(--jp-warn-color2);
    border-radius: var(--jp-border-radius);
    color: var(--jp-ui-font-color1);
    font-size: var(--jp-ui-font-size1);
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  .jp-RenderedMermaid figure {
    margin: 0;
    overflow: auto;
    max-width: 100%;
  }

  .jp-RenderedMermaid img {
    max-width: 100%;
  }

  .jp-RenderedMermaid-Details > pre {
    margin-top: 1em;
  }

  .jp-RenderedMermaid-Summary {
    color: var(--jp-warn-color2);
  }

  .jp-RenderedMermaid:not(.jp-mod-warning) pre {
    display: none;
  }

  .jp-RenderedMermaid-Summary > pre {
    display: inline-block;
    white-space: normal;
  }
</style>
<!-- End of mermaid configuration --></head>
<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">
<main>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=ae4915db-8035-4c92-b3c7-64a9053573d7">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><font size="+3"><strong>2.5. Predicting Apartment Prices in Mexico City 🇲🇽</strong></font></p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=24b9800e-3a72-4b08-af3d-65da4d226b69">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [2]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">warnings</span>

<span class="n">warnings</span><span class="o">.</span><span class="n">simplefilter</span><span class="p">(</span><span class="n">action</span><span class="o">=</span><span class="s2">"ignore"</span><span class="p">,</span> <span class="n">category</span><span class="o">=</span><span class="ne">FutureWarning</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=e7b2f0fe-fdcf-4c4e-8243-de6bd3f3bffc">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>In this assignment, you'll decide which libraries you need to complete the tasks. You can import them in the cell below. 👇</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=0cd1db04-5733-4a88-8216-210aa4b19c2d">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [1]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># Import libraries here</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">warnings</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">glob</span><span class="w"> </span><span class="kn">import</span> <span class="n">glob</span>

<span class="kn">import</span><span class="w"> </span><span class="nn">matplotlib.pyplot</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">plt</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">numpy</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">np</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">pandas</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">pd</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">category_encoders</span><span class="w"> </span><span class="kn">import</span> <span class="n">OneHotEncoder</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">sklearn.linear_model</span><span class="w"> </span><span class="kn">import</span> <span class="n">LinearRegression</span><span class="p">,</span> <span class="n">Ridge</span>  <span class="c1"># noqa F401</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">sklearn.metrics</span><span class="w"> </span><span class="kn">import</span> <span class="n">mean_absolute_error</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">sklearn.pipeline</span><span class="w"> </span><span class="kn">import</span> <span class="n">make_pipeline</span>

<span class="n">warnings</span><span class="o">.</span><span class="n">simplefilter</span><span class="p">(</span><span class="n">action</span><span class="o">=</span><span class="s2">"ignore"</span><span class="p">,</span> <span class="n">category</span><span class="o">=</span><span class="ne">FutureWarning</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=79e44a81-1eef-4bc6-8151-1a86d5844fb4">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Prepare-Data">Prepare Data<a class="anchor-link" href="#Prepare-Data">¶</a></h1>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=99c6bc6c-50d9-4e5c-9289-a6ef21d43bfd">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="Import">Import<a class="anchor-link" href="#Import">¶</a></h2>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=3b3dccdb-08cc-4e5b-bd8a-509114410864">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><strong>Task 2.5.1</strong></p>
<div class="alert alert-block alert-info">
<b>Tip:</b> Don't try to satisfy all the criteria in the first version of your <code>wrangle</code> function. Instead, work iteratively. Start with the first criteria, test it out with one of the Mexico CSV files in the <code>data/</code> directory, and submit it to the grader for feedback. Then add the next criteria.</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=8a585163-e2a9-4b46-8cf7-24ff8b00f0c0">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [21]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="k">def</span><span class="w"> </span><span class="nf">wrangle</span><span class="p">(</span><span class="n">filepath</span><span class="p">):</span>
    <span class="c1"># Read CSV file</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">filepath</span><span class="p">)</span>

    <span class="c1"># Subset data: Apartments in "Capital Federal", less than 400,000</span>
    <span class="n">mask_ba</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s2">"place_with_parent_names"</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">contains</span><span class="p">(</span><span class="s2">"Capital Federal"</span><span class="p">)</span>
    <span class="n">mask_apt</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s2">"property_type"</span><span class="p">]</span> <span class="o">==</span> <span class="s2">"apartment"</span>
    <span class="n">mask_price</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s2">"price_aprox_usd"</span><span class="p">]</span> <span class="o">&lt;</span> <span class="mi">400_000</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="n">mask_ba</span> <span class="o">&amp;</span> <span class="n">mask_apt</span> <span class="o">&amp;</span> <span class="n">mask_price</span><span class="p">]</span>

    <span class="c1"># Subset data: Remove outliers for "surface_covered_in_m2"</span>
    <span class="n">low</span><span class="p">,</span> <span class="n">high</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s2">"surface_covered_in_m2"</span><span class="p">]</span><span class="o">.</span><span class="n">quantile</span><span class="p">([</span><span class="mf">0.1</span><span class="p">,</span> <span class="mf">0.9</span><span class="p">])</span>
    <span class="n">mask_area</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s2">"surface_covered_in_m2"</span><span class="p">]</span><span class="o">.</span><span class="n">between</span><span class="p">(</span><span class="n">low</span><span class="p">,</span> <span class="n">high</span><span class="p">)</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="n">mask_area</span><span class="p">]</span>

    <span class="c1"># Split "lat-lon" column</span>
    <span class="n">df</span><span class="p">[[</span><span class="s2">"lat"</span><span class="p">,</span> <span class="s2">"lon"</span><span class="p">]]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s2">"lat-lon"</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">","</span><span class="p">,</span> <span class="n">expand</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">float</span><span class="p">)</span>
    <span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="s2">"lat-lon"</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="c1"># Get place name</span>
    <span class="n">df</span><span class="p">[</span><span class="s2">"neighborhood"</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s2">"place_with_parent_names"</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"|"</span><span class="p">,</span> <span class="n">expand</span><span class="o">=</span><span class="kc">True</span><span class="p">)[</span><span class="mi">3</span><span class="p">]</span>
    <span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="s2">"place_with_parent_names"</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

   
    <span class="k">return</span> <span class="n">df</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=345d00ac-9305-493b-8bbd-57aa9761f7ac">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [2]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">frame1</span> <span class="o">=</span> <span class="n">wrangle</span><span class="p">(</span><span class="s2">"data/mexico-city-real-estate-1.csv"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">frame1</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr" tabindex="0">
<pre>
<span class="ansi-red-fg">---------------------------------------------------------------------------</span>
<span class="ansi-red-fg">NameError</span>                                 Traceback (most recent call last)
Cell <span class="ansi-green-fg">In[2], line 1</span>
<span class="ansi-green-fg">----&gt; 1</span> frame1 <span style="color: rgb(98,98,98)">=</span> <span class="ansi-yellow-bg">wrangle</span>(<span style="color: rgb(175,0,0)">"</span><span style="color: rgb(175,0,0)">data/mexico-city-real-estate-1.csv</span><span style="color: rgb(175,0,0)">"</span>)
<span class="ansi-green-intense-fg ansi-bold">      2</span> <span style="color: rgb(0,135,0)">print</span>(frame1<span style="color: rgb(98,98,98)">.</span>head())

<span class="ansi-red-fg">NameError</span>: name 'wrangle' is not defined</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=f47ef1c8-b073-47a1-beba-028cd71500a6">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><strong>Task 2.5.2</strong></p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=db087948-57b5-4feb-931c-a51830b96b03">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [25]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">files</span> <span class="o">=</span> <span class="n">glob</span><span class="p">(</span><span class="s2">"data/mexico-city-real-estate-*.csv"</span><span class="p">)</span>
<span class="n">files</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
<span class="n">frames</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">files</span><span class="p">:</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">wrangle</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="n">frames</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">files</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr" tabindex="0">
<pre>
<span class="ansi-red-fg">---------------------------------------------------------------------------</span>
<span class="ansi-red-fg">ValueError</span>                                Traceback (most recent call last)
Cell <span class="ansi-green-fg">In[25], line 5</span>
<span class="ansi-green-intense-fg ansi-bold">      3</span> frames <span style="color: rgb(98,98,98)">=</span> []
<span class="ansi-green-intense-fg ansi-bold">      4</span> <span class="ansi-bold" style="color: rgb(0,135,0)">for</span> file <span class="ansi-bold" style="color: rgb(175,0,255)">in</span> files:
<span class="ansi-green-fg">----&gt; 5</span>     df <span style="color: rgb(98,98,98)">=</span> <span class="ansi-yellow-bg">wrangle</span><span class="ansi-yellow-bg">(</span><span class="ansi-yellow-bg">file</span><span class="ansi-yellow-bg">)</span>
<span class="ansi-green-intense-fg ansi-bold">      6</span>     frames<span style="color: rgb(98,98,98)">.</span>append(df)
<span class="ansi-green-intense-fg ansi-bold">      7</span> <span style="color: rgb(0,135,0)">print</span>(files)

Cell <span class="ansi-green-fg">In[21], line 17</span>, in <span class="ansi-cyan-fg">wrangle</span><span class="ansi-blue-fg">(filepath)</span>
<span class="ansi-green-intense-fg ansi-bold">     14</span> df <span style="color: rgb(98,98,98)">=</span> df[mask_area]
<span class="ansi-green-intense-fg ansi-bold">     16</span> <span style="color: rgb(95,135,135)"># Split "lat-lon" column</span>
<span class="ansi-green-fg">---&gt; 17</span> <span class="ansi-yellow-bg">df</span><span class="ansi-yellow-bg">[</span><span class="ansi-yellow-bg">[</span><span class="ansi-yellow-bg" style="color: rgb(175,0,0)">"</span><span class="ansi-yellow-bg" style="color: rgb(175,0,0)">lat</span><span class="ansi-yellow-bg" style="color: rgb(175,0,0)">"</span><span class="ansi-yellow-bg">,</span><span class="ansi-yellow-bg"> </span><span class="ansi-yellow-bg" style="color: rgb(175,0,0)">"</span><span class="ansi-yellow-bg" style="color: rgb(175,0,0)">lon</span><span class="ansi-yellow-bg" style="color: rgb(175,0,0)">"</span><span class="ansi-yellow-bg">]</span><span class="ansi-yellow-bg">]</span> <span style="color: rgb(98,98,98)">=</span> df[<span style="color: rgb(175,0,0)">"</span><span style="color: rgb(175,0,0)">lat-lon</span><span style="color: rgb(175,0,0)">"</span>]<span style="color: rgb(98,98,98)">.</span>str<span style="color: rgb(98,98,98)">.</span>split(<span style="color: rgb(175,0,0)">"</span><span style="color: rgb(175,0,0)">,</span><span style="color: rgb(175,0,0)">"</span>, expand<span style="color: rgb(98,98,98)">=</span><span class="ansi-bold" style="color: rgb(0,135,0)">True</span>)<span style="color: rgb(98,98,98)">.</span>astype(<span style="color: rgb(0,135,0)">float</span>)
<span class="ansi-green-intense-fg ansi-bold">     18</span> df<span style="color: rgb(98,98,98)">.</span>drop(columns<span style="color: rgb(98,98,98)">=</span><span style="color: rgb(175,0,0)">"</span><span style="color: rgb(175,0,0)">lat-lon</span><span style="color: rgb(175,0,0)">"</span>, inplace<span style="color: rgb(98,98,98)">=</span><span class="ansi-bold" style="color: rgb(0,135,0)">True</span>)
<span class="ansi-green-intense-fg ansi-bold">     20</span> <span style="color: rgb(95,135,135)"># Get place name</span>

File <span class="ansi-green-fg">/usr/local/lib/python3.11/site-packages/pandas/core/frame.py:3968</span>, in <span class="ansi-cyan-fg">DataFrame.__setitem__</span><span class="ansi-blue-fg">(self, key, value)</span>
<span class="ansi-green-intense-fg ansi-bold">   3966</span>     <span style="color: rgb(0,135,0)">self</span><span style="color: rgb(98,98,98)">.</span>_setitem_frame(key, value)
<span class="ansi-green-intense-fg ansi-bold">   3967</span> <span class="ansi-bold" style="color: rgb(0,135,0)">elif</span> <span style="color: rgb(0,135,0)">isinstance</span>(key, (Series, np<span style="color: rgb(98,98,98)">.</span>ndarray, <span style="color: rgb(0,135,0)">list</span>, Index)):
<span class="ansi-green-fg">-&gt; 3968</span>     <span class="ansi-yellow-bg" style="color: rgb(0,135,0)">self</span><span class="ansi-yellow-bg" style="color: rgb(98,98,98)">.</span><span class="ansi-yellow-bg">_setitem_array</span><span class="ansi-yellow-bg">(</span><span class="ansi-yellow-bg">key</span><span class="ansi-yellow-bg">,</span><span class="ansi-yellow-bg"> </span><span class="ansi-yellow-bg">value</span><span class="ansi-yellow-bg">)</span>
<span class="ansi-green-intense-fg ansi-bold">   3969</span> <span class="ansi-bold" style="color: rgb(0,135,0)">elif</span> <span style="color: rgb(0,135,0)">isinstance</span>(value, DataFrame):
<span class="ansi-green-intense-fg ansi-bold">   3970</span>     <span style="color: rgb(0,135,0)">self</span><span style="color: rgb(98,98,98)">.</span>_set_item_frame_value(key, value)

File <span class="ansi-green-fg">/usr/local/lib/python3.11/site-packages/pandas/core/frame.py:4010</span>, in <span class="ansi-cyan-fg">DataFrame._setitem_array</span><span class="ansi-blue-fg">(self, key, value)</span>
<span class="ansi-green-intense-fg ansi-bold">   4005</span> <span class="ansi-bold" style="color: rgb(0,135,0)">else</span>:
<span class="ansi-green-intense-fg ansi-bold">   4006</span>     <span style="color: rgb(95,135,135)"># Note: unlike self.iloc[:, indexer] = value, this will</span>
<span class="ansi-green-intense-fg ansi-bold">   4007</span>     <span style="color: rgb(95,135,135)">#  never try to overwrite values inplace</span>
<span class="ansi-green-intense-fg ansi-bold">   4009</span>     <span class="ansi-bold" style="color: rgb(0,135,0)">if</span> <span style="color: rgb(0,135,0)">isinstance</span>(value, DataFrame):
<span class="ansi-green-fg">-&gt; 4010</span>         <span class="ansi-yellow-bg">check_key_length</span><span class="ansi-yellow-bg">(</span><span class="ansi-yellow-bg" style="color: rgb(0,135,0)">self</span><span class="ansi-yellow-bg" style="color: rgb(98,98,98)">.</span><span class="ansi-yellow-bg">columns</span><span class="ansi-yellow-bg">,</span><span class="ansi-yellow-bg"> </span><span class="ansi-yellow-bg">key</span><span class="ansi-yellow-bg">,</span><span class="ansi-yellow-bg"> </span><span class="ansi-yellow-bg">value</span><span class="ansi-yellow-bg">)</span>
<span class="ansi-green-intense-fg ansi-bold">   4011</span>         <span class="ansi-bold" style="color: rgb(0,135,0)">for</span> k1, k2 <span class="ansi-bold" style="color: rgb(175,0,255)">in</span> <span style="color: rgb(0,135,0)">zip</span>(key, value<span style="color: rgb(98,98,98)">.</span>columns):
<span class="ansi-green-intense-fg ansi-bold">   4012</span>             <span style="color: rgb(0,135,0)">self</span>[k1] <span style="color: rgb(98,98,98)">=</span> value[k2]

File <span class="ansi-green-fg">/usr/local/lib/python3.11/site-packages/pandas/core/indexers/utils.py:401</span>, in <span class="ansi-cyan-fg">check_key_length</span><span class="ansi-blue-fg">(columns, key, value)</span>
<span class="ansi-green-intense-fg ansi-bold">    399</span> <span class="ansi-bold" style="color: rgb(0,135,0)">if</span> columns<span style="color: rgb(98,98,98)">.</span>is_unique:
<span class="ansi-green-intense-fg ansi-bold">    400</span>     <span class="ansi-bold" style="color: rgb(0,135,0)">if</span> <span style="color: rgb(0,135,0)">len</span>(value<span style="color: rgb(98,98,98)">.</span>columns) <span style="color: rgb(98,98,98)">!=</span> <span style="color: rgb(0,135,0)">len</span>(key):
<span class="ansi-green-fg">--&gt; 401</span>         <span class="ansi-bold" style="color: rgb(0,135,0)">raise</span> <span class="ansi-bold" style="color: rgb(215,95,95)">ValueError</span>(<span style="color: rgb(175,0,0)">"</span><span style="color: rgb(175,0,0)">Columns must be same length as key</span><span style="color: rgb(175,0,0)">"</span>)
<span class="ansi-green-intense-fg ansi-bold">    402</span> <span class="ansi-bold" style="color: rgb(0,135,0)">else</span>:
<span class="ansi-green-intense-fg ansi-bold">    403</span>     <span style="color: rgb(95,135,135)"># Missing keys in columns are represented as -1</span>
<span class="ansi-green-intense-fg ansi-bold">    404</span>     <span class="ansi-bold" style="color: rgb(0,135,0)">if</span> <span style="color: rgb(0,135,0)">len</span>(columns<span style="color: rgb(98,98,98)">.</span>get_indexer_non_unique(key)[<span style="color: rgb(98,98,98)">0</span>]) <span style="color: rgb(98,98,98)">!=</span> <span style="color: rgb(0,135,0)">len</span>(value<span style="color: rgb(98,98,98)">.</span>columns):

<span class="ansi-red-fg">ValueError</span>: Columns must be same length as key</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=5ddea2e2-0b77-4115-9659-90508261c8f7">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><strong>Task 2.5.3</strong></p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=a4cbe7ee-ab23-4337-9a93-03303bc7f91e">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [7]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">([</span><span class="n">wrangle</span><span class="p">(</span><span class="n">f</span><span class="p">)</span> <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">files</span><span class="p">],</span> <span class="n">ignore_index</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">info</span><span class="p">())</span>
<span class="n">df</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 5473 entries, 0 to 5472
Data columns (total 5 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   price_aprox_usd        5473 non-null   float64
 1   surface_covered_in_m2  5473 non-null   float64
 2   lat                    5149 non-null   float64
 3   lon                    5149 non-null   float64
 4   borough                5473 non-null   object 
dtypes: float64(4), object(1)
memory usage: 213.9+ KB
None
</pre>
</div>
</div>
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[7]:</div>
<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html" tabindex="0">
<div>
<style scoped="">
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
<thead>
<tr style="text-align: right;">
<th></th>
<th>price_aprox_usd</th>
<th>surface_covered_in_m2</th>
<th>lat</th>
<th>lon</th>
<th>borough</th>
</tr>
</thead>
<tbody>
<tr>
<th>0</th>
<td>94022.66</td>
<td>57.0</td>
<td>23.634501</td>
<td>-102.552788</td>
<td>Benito Juárez</td>
</tr>
<tr>
<th>1</th>
<td>70880.12</td>
<td>56.0</td>
<td>19.402413</td>
<td>-99.095391</td>
<td>Iztacalco</td>
</tr>
<tr>
<th>2</th>
<td>68228.99</td>
<td>80.0</td>
<td>19.357820</td>
<td>-99.149406</td>
<td>Benito Juárez</td>
</tr>
<tr>
<th>3</th>
<td>24235.78</td>
<td>60.0</td>
<td>19.504985</td>
<td>-99.208557</td>
<td>Azcapotzalco</td>
</tr>
<tr>
<th>4</th>
<td>94140.20</td>
<td>50.0</td>
<td>19.354219</td>
<td>-99.126244</td>
<td>Coyoacán</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=de2683ec-8324-4f60-b4ec-fcb316770512">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="Explore">Explore<a class="anchor-link" href="#Explore">¶</a></h2>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=f2811333-79a6-4708-8f05-c39e42efa804">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<div class="alert alert-info" role="alert">
<strong>Slight Code Change</strong>
<p>In the following task, you'll notice a small change in how plots are created compared to what you saw in the lessons.
While the lessons use the global matplotlib method like <code>plt.plot(...)</code>, in this task, you are expected to use the object-oriented (OOP) API instead.
This means creating your plots using <code>fig, ax = plt.subplots()</code> and then calling plotting methods on the <code>ax</code> object, such as <code>ax.plot(...)</code>, <code>ax.hist(...)</code>, or <code>ax.scatter(...)</code>.</p>
<p>If you're using pandas’ or seaborn’s built-in plotting methods (like <code>df.plot()</code> or <code>sns.lineplot()</code>), make sure to pass the <code>ax=ax</code> argument so that the plot is rendered on the correct axes.</p>
<p>This approach is considered best practice and will be used consistently across all graded tasks that involve matplotlib.</p>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=c49a4444-adb3-4193-b8d8-db7596c441e1">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><strong>Task 2.5.4</strong></p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=61ffe4f7-17bf-4ad7-9c22-45c041baa4a8">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [8]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span> 

<span class="c1"># Plot the histogram on the axes object</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s2">"price_aprox_usd"</span><span class="p">])</span> 

<span class="c1"># Label axes using the axes </span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s2">"Price [$]"</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s2">"Count"</span><span class="p">)</span>


<span class="c1"># Add title </span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">"Distribution of Apartment Prices"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[8]:</div>
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>Text(0.5, 1.0, 'Distribution of Apartment Prices')</pre>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAkgAAAHHCAYAAABEEKc/AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAAA+XUlEQVR4nO3deVxWZf7/8feNrKKAK0hupOZerhlqWUmioY2jjdmQaWNpBq6NpplmVmrWmGmm1UzqL3UsnVKz1Ai3SnKh3Jd0XFMBJwJcQeH6/dGD8+0+oAIi962+no/H/Xh4X9d1zvmcczTenXOdg8MYYwQAAACLh6sLAAAAcDcEJAAAABsCEgAAgA0BCQAAwIaABAAAYENAAgAAsCEgAQAA2BCQAAAAbAhIAAAANgQkoIDGjRsnh8NRItu6//77df/991vf165dK4fDocWLF5fI9vv06aOaNWuWyLaK6syZM3r66acVEhIih8OhIUOGuLokXAcOh0Pjxo1zdRm4BRGQcEuaM2eOHA6H9fH19VVoaKgiIyM1bdo0nT59uli2c+LECY0bN05bt24tlvUVJ3eurSAmTJigOXPmaMCAAfr444/Vq1evqy6TnZ2t0NBQORwOrVixogSqvLJz585p3LhxWrt2ratLKZCvvvqqUGHl/vvvd/p3Vr58ebVs2VIfffSRcnJyrl+hQHEwwC1o9uzZRpIZP368+fjjj81HH31kJkyYYDp06GAcDoepUaOG2bZtm9MyFy9eNOfPny/UdjZv3mwkmdmzZxdquczMTJOZmWl9X7NmjZFkFi1aVKj1FLW2rKwsc+HChWLb1vXQqlUr06ZNm0It8/XXXxtJpmbNmiY6Ovo6VVZwp06dMpLMyy+/7OpSCiQmJsYU5sdGu3btTNWqVc3HH39sPv74YzNlyhTTpEkTI8m88MILBVrH+fPnzcWLF4taMlBknq6LZoDrderUSS1atLC+jxo1SqtXr1bnzp31yCOPaM+ePfLz85MkeXp6ytPz+v6TOXfunEqXLi1vb+/rup2r8fLycun2CyIlJUUNGjQo1DLz5s1Ts2bN1Lt3b7344os6e/as/P39r1OFl5eTk6OsrKwS364rBAYG6oknnrC+9+/fX3Xr1tW7776rV199Nd+/a7nHx9fXV76+viVZLmDhFhtg8+CDD2rMmDE6cuSI5s2bZ7XnNwcpLi5Obdu2VVBQkMqUKaO6devqxRdflPT7vKGWLVtKkp566inrNsOcOXMk/X77oVGjRkpMTNR9992n0qVLW8va5yDlys7O1osvvqiQkBD5+/vrkUce0bFjx5zG1KxZU3369Mmz7B/XebXa8puDdPbsWT3//POqVq2afHx8VLduXb311lsyxjiNczgcio2N1ZIlS9SoUSP5+PioYcOGWrlyZf4H3CYlJUV9+/ZVcHCwfH19ddddd2nu3LlWf+58rEOHDunLL7+0aj98+PAV13v+/Hl9/vnn6tmzp3r06KHz589r6dKlecb16dNHZcqU0cGDBxUZGSl/f3+FhoZq/Pjxefb1rbfeUuvWrVWhQgX5+fmpefPm+c4Tyz0m8+fPV8OGDeXj46NZs2apUqVKkqRXXnnF2o/cW1i5dRw9elSdO3dWmTJldNttt2nGjBmSpB07dujBBx+Uv7+/atSooQULFuTZblpamoYMGWKds9q1a+uNN95wur11+PBhORwOvfXWW/rggw9Uq1Yt+fj4qGXLltq8ebPTccnd9h9vmxVW6dKldc899+js2bM6derUZY9P7t+X/OYgHT9+XH379lVoaKh8fHwUFhamAQMGOIXOguy7JC1cuFDNmzdX2bJlFRAQoMaNG+udd94p9H7h5sMVJCAfvXr10osvvqivv/5azzzzTL5jdu3apc6dO+vOO+/U+PHj5ePjowMHDuj777+XJNWvX1/jx4/X2LFj1a9fP917772SpNatW1vr+PXXX9WpUyf17NlTTzzxhIKDg69Y1+uvvy6Hw6EXXnhBKSkpmjp1qiIiIrR161brSldBFKS2PzLG6JFHHtGaNWvUt29fNWnSRKtWrdLw4cN1/Phxvf32207jv/vuO3322Wd67rnnVLZsWU2bNk3du3fX0aNHVaFChcvWdf78ed1///06cOCAYmNjFRYWpkWLFqlPnz5KS0vT4MGDVb9+fX388ccaOnSoqlatqueff16SrLBxOcuWLdOZM2fUs2dPhYSE6P7779f8+fP117/+Nc/Y7OxsdezYUffcc48mT56slStX6uWXX9alS5c0fvx4a9w777yjRx55RNHR0crKytLChQv1l7/8RcuXL1dUVJTTOlevXq1PP/1UsbGxqlixou666y7NnDlTAwYM0J///Gd169ZNknTnnXc61dGpUyfdd999mjx5subPn6/Y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tfTqq6/KGGONMcZo7NixqlKlivz8/BQREaH9+/c7rSc1NVXR0dEKCAhQUFCQ+vbtqzNnzpT07gAAgBuEWwekN954QzNnztS7776rPXv26I033tDkyZM1ffp0a8zkyZM1bdo0zZo1Sxs3bpS/v78iIyN14cIFa0x0dLR27dqluLg4LV++XOvXr1e/fv1csUsAAOAG4DB/vBzjZjp37qzg4GD961//stq6d+8uPz8/zZs3T8YYhYaG6vnnn9ff//53SVJ6erqCg4M1Z84c9ezZU3v27FGDBg20efNmtWjRQpK0cuVKPfzww/rll18UGhp61ToyMjIUGBio9PR0BQQEXJ+dBfJRc+SXri7hlnB4UpSrSwBwHVzLz2+3voLUunVrxcfH6+eff5Ykbdu2Td999506deokSTp06JCSkpIUERFhLRMYGKhWrVopISFBkpSQkKCgoCArHElSRESEPDw8tHHjxny3m5mZqYyMDKcPAAC4dXi6uoArGTlypDIyMlSvXj2VKlVK2dnZev311xUdHS1JSkpKkiQFBwc7LRccHGz1JSUlqXLlyk79np6eKl++vDXGbuLEiXrllVeKe3cAAMANwq2vIH366aeaP3++FixYoB9//FFz587VW2+9pblz517X7Y4aNUrp6enW59ixY9d1ewAAwL249RWk4cOHa+TIkerZs6ckqXHjxjpy5IgmTpyo3r17KyQkRJKUnJysKlWqWMslJyerSZMmkqSQkBClpKQ4rffSpUtKTU21lrfz8fGRj4/PddgjAABwI3DrK0jnzp2Th4dziaVKlVJOTo4kKSwsTCEhIYqPj7f6MzIytHHjRoWHh0uSwsPDlZaWpsTERGvM6tWrlZOTo1atWpXAXgAAgBuNW19B6tKli15//XVVr15dDRs21E8//aQpU6bob3/7myTJ4XBoyJAheu2111SnTh2FhYVpzJgxCg0NVdeuXSVJ9evXV8eOHfXMM89o1qxZunjxomJjY9WzZ88CPcEGAABuPW4dkKZPn64xY8boueeeU0pKikJDQ9W/f3+NHTvWGjNixAidPXtW/fr1U1pamtq2bauVK1fK19fXGjN//nzFxsaqffv28vDwUPfu3TVt2jRX7BIAALgBuPV7kNwF70GCq/AepJLBe5CAm9NN+x4kAAAAVyAgAQAA2BCQAAAAbAhIAAAANgQkAAAAGwIS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evSooqKiVLp0aVWuXFnDhw/XpUuXSnJXAADADcStA9K6desUExOjH374QXFxcbp48aI6dOigs2fPWmOGDh2qL774QosWLdK6det04sQJdevWzerPzs5WVFSUsrKytGHDBs2dO1dz5szR2LFjXbFLAADgBuAwxhhXF1FQp06dUuXKlbVu3Trdd999Sk9PV6VKlbRgwQI9+uijkqS9e/eqfv36SkhI0D333KMVK1aoc+fOOnHihIKDgyVJs2bN0gsvvKBTp07J29v7qtvNyMhQYGCg0tPTFRAQcF338UZRc+SXri4BAHATOTwpqtjXeS0/v936CpJdenq6JKl8+fKSpMTERF28eFERERHWmHr16ql69epKSEiQJCUkJKhx48ZWOJKkyMhIZWRkaNeuXfluJzMzUxkZGU4fAABw67hhAlJOTo6GDBmiNm3aqFGjRpKkpKQkeXt7KygoyGlscHCwkpKSrDF/DEe5/bl9+Zk4caICAwOtT7Vq1Yp5bwAAgDu7YQJSTEyMdu7cqYULF173bY0aNUrp6enW59ixY9d9mwAAwH14urqAgoiNjdXy5cu1fv16Va1a1WoPCQlRVlaW0tLSnK4iJScnKyQkxBqzadMmp/XlPuWWO8bOx8dHPj4+xbwXAADgRuHWV5CMMYqNjdXnn3+u1atXKywszKm/efPm8vLyUnx8vNW2b98+HT16VOHh4ZKk8PBw7dixQykpKdaYuLg4BQQEqEGDBiWzIwAA4Ibi1leQYmJitGDBAi1dulRly5a15gwFBgbKz89PgYGB6tu3r4YNG6by5csrICBAAwcOVHh4uO655x5JUocOHdSgQQP16tVLkydPVlJSkl566SXFxMRwlQgAAOTLrQPSzJkzJUn333+/U/vs2bPVp08fSdLbb78tDw8Pde/eXZmZmYqMjNR7771njS1VqpSWL1+uAQMGKDw8XP7+/urdu7fGjx9fUrsBAABuMDfUe5Bchfcg5cV7kAAAxYn3IAEAALg5AhIAAIANAQkAAMCGgAQAAGBDQAIAALAhIAEAANgQkAAAAGwISAAAADYEJAAAABsCEgAAgA0BCQAAwIaABAAAYENAAgAAsCEgAQAA2BCQAAAAbAhIAAAANgQkAAAAGwISAACADQEJAADAhoAEAABgQ0ACAACwISABAADYEJAAAABsCEgAAAA2BCQAAAAbAhIAAIANAQkAAMCGgAQAAGBDQAIAALAhIAEAANgQkAAAAGwISAAAADYEJAAAABsCEgAAgA0BCQAAwIaABAAAYENAAgAAsCEgAQAA2BCQAAAAbAhIAAAANgQkAAAAGwISAACADQEJAADAhoAEAABgQ0ACAACwISABAADYEJAAAABsCEgAAAA2BCQAAAAbT1cXAKnmyC9dXQIAAPgDriABAADYEJAAAABsCEgAAAA2BCQAAAAbAhIAAIANAQkAAMDmlgpIM2bMUM2aNeXr66tWrVpp06ZNri4JAAC4oVsmIH3yyScaNmyYXn75Zf3444+66667FBkZqZSUFFeXBgAA3MwtE5CmTJmiZ555Rk899ZQaNGigWbNmqXTp0vroo49cXRoAAHAzt0RAysrKUmJioiIiIqw2Dw8PRUREKCEhwYWVAQAAd3RL/KqR//3vf8rOzlZwcLBTe3BwsPbu3ZtnfGZmpjIzM63v6enpkqSMjIzrUl9O5rnrsl4AAG4U1+NnbO46jTGFXvaWCEiFNXHiRL3yyit52qtVq+aCagAAuPkFTr1+6z59+rQCAwMLtcwtEZAqVqyoUqVKKTk52ak9OTlZISEhecaPGjVKw4YNs77n5OQoNTVVFSpUkMPhuO713swyMjJUrVo1HTt2TAEBAa4u55bFeXAPnAf3wHlwD9fjPBhjdPr0aYWGhhZ62VsiIHl7e6t58+aKj49X165dJf0eeuLj4xUbG5tnvI+Pj3x8fJzagoKCSqDSW0dAQAD/IXIDnAf3wHlwD5wH91Dc56GwV45y3RIBSZKGDRum3r17q0WLFrr77rs1depUnT17Vk899ZSrSwMAAG7mlglIjz32mE6dOqWxY8cqKSlJTZo00cqVK/NM3AYAALhlApIkxcbG5ntLDSXHx8dHL7/8cp5bmChZnAf3wHlwD5wH9+Bu58FhivLsGwAAwE3slnhRJAAAQGEQkAAAAGwISAAAADYEJAAAABsCEq5o4sSJatmypcqWLavKlSura9eu2rdvn9OYCxcuKCYmRhUqVFCZMmXUvXv3PG8tP3r0qKKiolS6dGlVrlxZw4cP16VLl5zGrF27Vs2aNZOPj49q166tOXPm5KlnxowZqlmzpnx9fdWqVStt2rSp2PfZ3U2aNEkOh0NDhgyx2jgHJef48eN64oknVKFCBfn5+alx48basmWL1W+M0dixY1WlShX5+fkpIiJC+/fvd1pHamqqoqOjFRAQoKCgIPXt21dnzpxxGrN9+3bde++98vX1VbVq1TR58uQ8tSxatEj16tWTr6+vGjdurK+++ur67LSbyc7O1pgxYxQWFiY/Pz/VqlVLr776qtPv2+I8FL/169erS5cuCg0NlcPh0JIlS5z63emYF6SWqzLAFURGRprZs2ebnTt3mq1bt5qHH37YVK9e3Zw5c8Ya8+yzz5pq1aqZ+Ph4s2XLFnPPPfeY1q1bW/2XLl0yjRo1MhEREeann34yX331lalYsaIZNWqUNebgwYOmdOnSZtiwYWb37t1m+vTpplSpUmblypXWmIULFxpvb2/z0UcfmV27dplnnnnGBAUFmeTk5JI5GG5g06ZNpmbNmubOO+80gwcPtto5ByUjNTXV1KhRw/Tp08ds3LjRHDx40KxatcocOHDAGjNp0iQTGBholixZYrZt22YeeeQRExYWZs6fP2+N6dixo7nrrrvMDz/8YL799ltTu3Zt8/jjj1v96enpJjg42ERHR5udO3eaf//738bPz8+8//771pjvv//elCpVykyePNns3r3bvPTSS8bLy8vs2LGjZA6GC73++uumQoUKZvny5ebQoUNm0aJFpkyZMuadd96xxnAeit9XX31lRo8ebT777DMjyXz++edO/e50zAtSy9UQkFAoKSkpRpJZt26dMcaYtLQ04+XlZRYtWmSN2bNnj5FkEhISjDG//6Py8PAwSUlJ1piZM2eagIAAk5mZaYwxZsSIEaZhw4ZO23rsscdMZGSk9f3uu+82MTEx1vfs7GwTGhpqJk6cWPw76oZOnz5t6tSpY+Li4ky7du2sgMQ5KDkvvPCCadu27WX7c3JyTEhIiHnzzTettrS0NOPj42P+/e9/G2OM2b17t5FkNm/ebI1ZsWKFcTgc5vjx48YYY9577z1Trlw569zkbrtu3brW9x49epioqCin7bdq1cr079//2nbyBhAVFWX+9re/ObV169bNREdHG2M4DyXBHpDc6ZgXpJaC4BYbCiU9PV2SVL58eUlSYmKiLl68qIiICGtMvXr1VL16dSUkJEiSEhIS1LhxY6e3lkdGRiojI0O7du2yxvxxHbljcteRlZWlxMREpzEeHh6KiIiwxtzsYmJiFBUVlec4cQ5KzrJly9SiRQv95S9/UeXKldW0aVN9+OGHVv+hQ4eUlJTkdIwCAwPVqlUrp3MRFBSkFi1aWGMiIiLk4eGhjRs3WmPuu+8+eXt7W2MiIyO1b98+/fbbb9aYK52vm1nr1q0VHx+vn3/+WZK0bds2fffdd+rUqZMkzoMruNMxL0gtBUFAQoHl5ORoyJAhatOmjRo1aiRJSkpKkre3d55f5hscHKykpCRrjP1XuuR+v9qYjIwMnT9/Xv/73/+UnZ2d75jcddzMFi5cqB9//FETJ07M08c5KDkHDx7UzJkzVadOHa1atUoDBgzQoEGDNHfuXEn/dyyvdIySkpJUuXJlp35PT0+VL1++WM7XrXAuRo4cqZ49e6pevXry8vJS06ZNNWTIEEVHR0viPLiCOx3zgtRSELfUrxrBtYmJidHOnTv13XffubqUW8qxY8c0ePBgxcXFydfX19Xl3NJycnLUokULTZgwQZLUtGlT7dy5U7NmzVLv3r1dXN2t49NPP9X8+fO1YMECNWzYUFu3btWQIUMUGhrKeUCx4QoSCiQ2NlbLly/XmjVrVLVqVas9JCREWVlZSktLcxqfnJyskJAQa4z9iarc71cbExAQID8/P1WsWFGlSpXKd0zuOm5WiYmJSklJUbNmzeTp6SlPT0+tW7dO06ZNk6enp4KDgzkHJaRKlSpq0KCBU1v9+vV19OhRSf93LK90jEJCQpSSkuLUf+nSJaWmphbL+boVzsXw4cOtq0iNGzdWr169NHToUOsKK+eh5LnTMS9ILQVBQMIVGWMUGxurzz//XKtXr1ZYWJhTf/PmzeXl5aX4+Hirbd++fTp69KjCw8MlSeHh4dqxY4fTP4y4uDgFBARYP2zCw8Od1pE7Jncd3t7eat68udOYnJwcxcfHW2NuVu3bt9eOHTu0detW69OiRQtFR0dbf+YclIw2bdrkec3Fzz//rBo1akiSwsLCFBIS4nSMMjIytHHjRqdzkZaWpsTERGvM6tWrlZOTo1atWllj1q9fr4sXL1pj4uLiVLduXZUrV84ac6XzdTM7d+6cPDycf3yVKlVKOTk5kjgPruBOx7wgtRRIgadz45Y0YMAAExgYaNauXWtOnjxpfc6dO2eNefbZZ0316tXN6tWrzZYtW0x4eLgJDw+3+nMfMe/QoYPZunWrWblypalUqVK+j5gPHz7c7Nmzx8yYMSPfR8x9fHzMnDlzzO7du02/fv1MUFCQ05NZt4o/PsVmDOegpGzatMl4enqa119/3ezfv9/Mnz/flC5d2sybN88aM2nSJBMUFGSWLl1qtm/fbv70pz/l+6hz06ZNzcaNG813331n6tSp4/Soc1pamgkODja9evUyO3fuNAsXLjSlS5fO86izp6eneeutt8yePXvMyy+/fNM+Xm7Xu3dvc9ttt1mP+X/22WemYsWKZsSIEdYYzkPxO336tPnpp5/MTz/9ZCSZKVOmmJ9++skcOXLEGONex7wgtVwNAQlXJCnfz+zZs60x58+fN88995wpV66cKV26tPnzn/9sTp486bSew4cPm06dOhk/Pz9TsWJF8/zzz5uLFy86jVmzZo1p0qSJ8fb2NrfffrvTNnJNnz7dVK9e3Xh7e5u7777b/PDDD9djt92ePSBxDkrOF198YRo1amR8fHxMvXr1zAcffODUn5OTY8aMGWOCg4ONj4+Pad++vdm3b5/TmF9//dU8/vjjpkyZMiYgIMA89dRT5vTp005jtm3bZtq2bWt8fHzMbbfdZiZNmpSnlk8//dTccccdxtvb2zRs2NB8+eWXxb/DbigjI8MMHjzYVK9e3fj6+prbb7/djB492unRcM5D8VuzZk2+Pw969+5tjHGvY16QWq7GYcwfXj0KAAAA5iABAADYEZAAAABsCEgAAAA2BCQAAAAbAhIAAIANAQkAAMCGgAQAAGBDQAJw06hZs6amTp163dY/btw4ORwOORyOfLezdu1azZkzJ99lc5cLCgq6bvUBKD4EJABup0+fPlag8Pb2Vu3atTV+/HhdunTpistt3rxZ/fr1u661NWzYUCdPniz0dk6ePHldwxuA4kVAAuCWOnbsqJMnT2r//v16/vnnNW7cOL355pv5js3KypIkVapUSaVLl76udXl6eiokJMRpO1u3btVDDz2k7t27a+DAgWrcuLHGjRvntFxISIgCAwOva20Aig8BCYBb8vHxUUhIiGrUqKEBAwYoIiJCy5Ytk/T7FaauXbvq9ddfV2hoqOrWrSsp7y22tLQ09e/fX8HBwfL19VWjRo20fPlyq/+7777TvffeKz8/P1WrVk2DBg3S2bNnC1WnMUZ/+tOf5Ofnp4kTJ2rEiBGaMGGC/Pz8rv0gAHAZT1cXAAAF4efnp19//dX6Hh8fr4CAAMXFxeU7PicnR506ddLp06c1b9481apVS7t371apUqUkSf/973/VsWNHvfbaa/roo4906tQpxcbGKjY2VrNnzy5wXb/++quOHj2qBQsW6OLFi/L29laXLl3UpUuXa9thAC5FQALg1owxio+P16pVqzRw4ECr3d/fX//85z/l7e2d73LffPONNm3apD179uiOO+6QJN1+++1W/8SJExUdHa0hQ4ZIkurUqaNp06apXbt2mjlzpnx9fQtUX8WKFVW3bl29+uqr6tixI5OwgZsEt9gAuKXly5erTJky8vX1VadOnfTYY485zetp3LjxZcOR9Pu8oKpVq1rhyG7btm2aM2eOypQpY30iIyOVk5OjQ4cOFarWVatWKTg4WBMmTNCzzz6r9u3ba/Xq1YVaBwD3whUkAG7pgQce0MyZM+Xt7a3Q0FB5ejr/58rf3/+Ky19tDtCZM2fUv39/DRo0KE9f9erVC1VrjRo1NHfuXK1du1Zr1qzRmTNn1LFjR/30009q2LBhodYFwD0QkAC4JX9/f9WuXbvIy99555365Zdf9PPPP+d7FalZs2bavXv3NW0jP2FhYerTp4/mzJmjH374gYAE3KC4xQbgptSuXTvdd9996t69u+Li4nTo0CGtWLFCK1eulCS98MIL2rBhg2JjY7V161bt379fS5cuVWxsbKG2c+LECQ0bNkzbt29XZmamzp07p/fff19paWlq2rTp9dg1ACWAK0gAblr/+c9/9Pe//12PP/64zp49q9q1a2vSpEmSfr/CtG7dOo0ePVr33nuvjDGqVauWHnvssUJtIyAgQJcuXdKjjz6qo0ePyhij22+/XbNnz1azZs2ux24BKAEOY4xxdREAcCMYN26clixZoq1bt+bbv3btWh0+fFh9+vTJt3/OnDkaMmSI0tLSrluNAIoHt9gAoBB27NihMmXK6L333ivUcmXKlNGzzz57naoCUNy4ggQABZSamqrU1FRJv/9ak8L86pADBw5IkkqVKqWwsLDrUh+A4kNAAgAAsOEWGwAAgA0BCQAAwIaABAAAYENAAgAAsCEgAQAA2BCQAAAAbAhIAAAANgQkAAAAGwISAACAzf8H6rt4pniZYGIAAAAASUVORK5CYII="/>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=3e4f18dc-04f3-451a-a772-0d605fb1b5a2">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><strong>Task 2.5.5</strong></p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=148d1a3f-37f7-4f6e-95b4-f7c725d95a66">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [9]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span> 

<span class="c1"># Create the scatter plot on the axes object</span>
<span class="n">ax</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span>
    <span class="n">df</span><span class="p">[</span><span class="s2">"surface_covered_in_m2"</span><span class="p">],</span>
    <span class="n">df</span><span class="p">[</span><span class="s2">"price_aprox_usd"</span><span class="p">],</span>
    <span class="p">)</span> 

<span class="c1"># Label axes </span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s2">"Area [sq meters]"</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s2">"Price [USD]"</span><span class="p">)</span>

<span class="c1">#  Add title </span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">"Mexico City: Price vs. Area"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[9]:</div>
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>Text(0.5, 1.0, 'Mexico City: Price vs. Area')</pre>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,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ZEijZR5HUlNTMXbsWHz44YdNqqJbrVb85S9/cfvvgQanwfFcHYmJicH111+Pzz77DEuXLsXYsWMRExNj//1SJRUuBbPZbK+k3LlzZ6Pf5Wt8++23Iy0tDT/99FMjm+LiYtTV1anua9KkScjOzsaHH36Iffv2NXIsCwsLG/2b3r17AwBqamrsf3f48OFGz4Irv/zyCzIzM3Hffffh1ltvbfTfpEmTsH79emRnZytuZ8yYMQgLC8OcOXPslayOyBIWchRNcqnyc1zeNDDQHG9myRsYGLjHsfpPCdfqP0mSpAceeEACIF1//fXSO++8Iy1YsEB67LHHpISEBOmrr76SJEmS0tPTpYCAAOnee++1/7ujR49KQUFB0m233Wb/u6aq//bu3SuFhIRI0dHR0owZM6RFixZJzz33nNSrVy+7zcGDB6Xg4GCpTZs20muvvSa9/vrrUocOHSR/f39p69atquefl5cn9e7dWzKZTNKNN94ozZ8/X/rwww+lZ599VkpMTJQsFovdtqnqv3HjxknBwcHS22+/LX3xxReN9vn1119LACQA0rJly5x+E63+69atm6odAOlPf/qT298cq//OnDkjxcXFSUFBQdLjjz8u/f3vf5dmzZoldevWzV4RWVFRIV111VWSr6+v9Mc//lH629/+Jr311lvSH/7wByk4OJiq2KuqqpJCQ0Ol0NBQycfHR8rNzXX6/bHHHpP69OkjvfDCC9LixYul1157TWrTpo3Utm1bp+pJANLw4cMV9/Xggw9KPj4+UkFBQZO/HzhwQAIgvf3225IkKT//S5culcxms9S9e3fp1Vdflf7+979Lzz//vNS7d2+nazxs2DApKChIev7556UPPvhAmjhxotSrV69G19vAQCsMp8rAoIVyKU6VJEnSokWLpL59+0qBgYFSaGio1KNHD+mZZ56RsrOzpbq6Oqlfv36NPo6SJEnz5893cjSacqokqcFpuvnmm6WIiAgpICBA6ty5szRz5kwnm927d0tjxoyRQkJCpKCgIOnaa6+VtmzZQl+DyspK6a233pL69esnhYSESBaLRbryyiulP//5z9Lx48ftdk05VYcPH5aGDRsmBQYGSgAaySvU1NRIkZGRUnh4uFRVVeX0m7edKkmSpKysLOmee+6RWrVqJfn7+0sdOnSQ/vSnP0k1NTV2m7KyMmnGjBnSFVdcIVks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"/>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=5670726a-411e-42d5-832f-d522d5b44a50">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>Do you see a relationship between price and area in the data? How is this similar to or different from the Buenos Aires dataset?<span style="color: transparent; font-size:1%">WQU WorldQuant University Applied Data Science Lab QQQQ</span></p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=095bc111-55a9-40c2-b322-4ab50c617750">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><strong>Task 2.5.6</strong> <strong>(UNGRADED)</strong> Create a Mapbox scatter plot that shows the location of the apartments in your dataset and represent their price using color.</p>
<p>What areas of the city seem to have higher real estate prices?</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=d07fc514-897c-4399-87e1-97c930bf8a66">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [10]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># Plot Mapbox location and price</span>

<span class="n">fig</span> <span class="o">=</span> <span class="n">px</span><span class="o">.</span><span class="n">scatter_mapbox</span><span class="p">(</span>
    <span class="n">df</span><span class="p">,</span>
    <span class="n">lat</span><span class="o">=...</span><span class="p">,</span>
    <span class="n">lon</span><span class="o">=...</span><span class="p">,</span>
    <span class="n">width</span><span class="o">=...</span><span class="p">,</span>
    <span class="n">height</span><span class="o">=...</span><span class="p">,</span>
    <span class="n">color</span><span class="o">=...</span><span class="p">,</span>
<span class="p">)</span>


<span class="n">fig</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr" tabindex="0">
<pre>
<span class="ansi-red-fg">---------------------------------------------------------------------------</span>
<span class="ansi-red-fg">NameError</span>                                 Traceback (most recent call last)
Cell <span class="ansi-green-fg">In[10], line 3</span>
<span class="ansi-green-intense-fg ansi-bold">      1</span> <span style="color: rgb(95,135,135)"># Plot Mapbox location and price</span>
<span class="ansi-green-fg">----&gt; 3</span> fig <span style="color: rgb(98,98,98)">=</span> <span class="ansi-yellow-bg">px</span><span style="color: rgb(98,98,98)">.</span>scatter_mapbox(
<span class="ansi-green-intense-fg ansi-bold">      4</span>     df,
<span class="ansi-green-intense-fg ansi-bold">      5</span>     lat<span style="color: rgb(98,98,98)">=</span><span style="color: rgb(98,98,98)">.</span><span style="color: rgb(98,98,98)">.</span><span style="color: rgb(98,98,98)">.</span>,
<span class="ansi-green-intense-fg ansi-bold">      6</span>     lon<span style="color: rgb(98,98,98)">=</span><span style="color: rgb(98,98,98)">.</span><span style="color: rgb(98,98,98)">.</span><span style="color: rgb(98,98,98)">.</span>,
<span class="ansi-green-intense-fg ansi-bold">      7</span>     width<span style="color: rgb(98,98,98)">=</span><span style="color: rgb(98,98,98)">.</span><span style="color: rgb(98,98,98)">.</span><span style="color: rgb(98,98,98)">.</span>,
<span class="ansi-green-intense-fg ansi-bold">      8</span>     height<span style="color: rgb(98,98,98)">=</span><span style="color: rgb(98,98,98)">.</span><span style="color: rgb(98,98,98)">.</span><span style="color: rgb(98,98,98)">.</span>,
<span class="ansi-green-intense-fg ansi-bold">      9</span>     color<span style="color: rgb(98,98,98)">=</span><span style="color: rgb(98,98,98)">.</span><span style="color: rgb(98,98,98)">.</span><span style="color: rgb(98,98,98)">.</span>,
<span class="ansi-green-intense-fg ansi-bold">     10</span> )
<span class="ansi-green-intense-fg ansi-bold">     13</span> fig<span style="color: rgb(98,98,98)">.</span>show()

<span class="ansi-red-fg">NameError</span>: name 'px' is not defined</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=1d9f5ee7-348c-407b-a8ce-b4a79f7a0cc4">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="Split">Split<a class="anchor-link" href="#Split">¶</a></h2>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=f943c3ec-c299-4941-996c-4ea4a21a14f5">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><strong>Task 2.5.7</strong></p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=eac77c6c-b0e3-4d84-af72-f75270c11187">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [8]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># Target vector</span>
<span class="n">y_train</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s2">"price_aprox_usd"</span><span class="p">]</span>

<span class="c1"># Feature matrix - all columns except the target column</span>
<span class="n">X_train</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="s2">"price_aprox_usd"</span><span class="p">])</span>

<span class="c1"># Check shapes to match expected outcome</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"X_train shape:"</span><span class="p">,</span> <span class="n">X_train</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>  <span class="c1"># Expected: (5473, 4)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"y_train shape:"</span><span class="p">,</span> <span class="n">y_train</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>  <span class="c1"># Expected: (5473,)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr" tabindex="0">
<pre>
<span class="ansi-red-fg">---------------------------------------------------------------------------</span>
<span class="ansi-red-fg">NameError</span>                                 Traceback (most recent call last)
Cell <span class="ansi-green-fg">In[8], line 2</span>
<span class="ansi-green-intense-fg ansi-bold">      1</span> <span style="color: rgb(95,135,135)"># Target vector</span>
<span class="ansi-green-fg">----&gt; 2</span> y_train <span style="color: rgb(98,98,98)">=</span> <span class="ansi-yellow-bg">df</span>[<span style="color: rgb(175,0,0)">"</span><span style="color: rgb(175,0,0)">price_aprox_usd</span><span style="color: rgb(175,0,0)">"</span>]
<span class="ansi-green-intense-fg ansi-bold">      4</span> <span style="color: rgb(95,135,135)"># Feature matrix - all columns except the target column</span>
<span class="ansi-green-intense-fg ansi-bold">      5</span> X_train <span style="color: rgb(98,98,98)">=</span> df<span style="color: rgb(98,98,98)">.</span>drop(columns<span style="color: rgb(98,98,98)">=</span>[<span style="color: rgb(175,0,0)">"</span><span style="color: rgb(175,0,0)">price_aprox_usd</span><span style="color: rgb(175,0,0)">"</span>])

<span class="ansi-red-fg">NameError</span>: name 'df' is not defined</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=df817f6c-ca21-49d0-be84-7af163041ca5">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Build-Model">Build Model<a class="anchor-link" href="#Build-Model">¶</a></h1>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=2ddaad75-ef9c-49c0-a963-4348483e7201">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="Baseline">Baseline<a class="anchor-link" href="#Baseline">¶</a></h2>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=6cdda106-0d7a-426d-aa9d-94ed60702c32">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><strong>Task 2.5.8</strong></p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=3a998470-7558-4c2a-8681-ea76d9b2ae16">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [13]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">from</span><span class="w"> </span><span class="nn">sklearn.metrics</span><span class="w"> </span><span class="kn">import</span> <span class="n">mean_absolute_error</span>

<span class="n">y_mean</span> <span class="o">=</span> <span class="n">y_train</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
<span class="n">y_pred_baseline</span> <span class="o">=</span> <span class="p">[</span><span class="n">y_mean</span><span class="p">]</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span><span class="n">y_train</span><span class="p">)</span>
<span class="n">baseline_mae</span> <span class="o">=</span> <span class="n">mean_absolute_error</span><span class="p">(</span><span class="n">y_train</span><span class="p">,</span> <span class="n">y_pred_baseline</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Mean apt price:"</span><span class="p">,</span> <span class="n">y_mean</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Baseline MAE:"</span><span class="p">,</span> <span class="nb">round</span><span class="p">(</span><span class="n">baseline_mae</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Mean apt price: 54246.5314982642
Baseline MAE: 17239.94
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=0b5e8c7d-dbd3-4405-a048-475a0150578b">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="Iterate">Iterate<a class="anchor-link" href="#Iterate">¶</a></h2>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=d43cc258-e24e-4231-8638-7b80df4636dc">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><strong>Task 2.5.9</strong></p>
</div>
</div>
</div>
</div># Transformations (Transformer)
#Instantiate
ohe = OneHotEncoder(use_cat_names=True)
#fit
ohe.fit(X_train)
#transform
XT_train = ohe.transform(X_train)
print(XT_train.shape)
XT_train.head()from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import Ridge

# detect columns
numeric_features = X_train.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_features = X_train.select_dtypes(exclude=["int64", "float64"]).columns.tolist()

# robust OneHotEncoder creation for different sklearn versions
try:
    ohe = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
except TypeError:  # older sklearn
    ohe = OneHotEncoder(handle_unknown="ignore", sparse=False)

# ColumnTransformer that encodes categorical cols and passes numeric through
onehot_ct = ColumnTransformer(
    transformers=[
        ("cat", ohe, categorical_features)
    ],
    remainder="passthrough"
)

# Pipeline with the exact step names expected by your tests
model = Pipeline(steps=[
    ("onehotencoder", onehot_ct),                    # encodes categories, leaves numeric
    ("simpleimputer", SimpleImputer(strategy="median")),  # fills any remaining NaNs
    ("ridge", Ridge())
])

# fit
model.fit(X_train, y_train)

# confirm step names
print(list(model.named_steps.keys()))  # -&gt; ['onehotencoder', 'simpleimputer', 'ridge']<div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=0e47136d-8fe7-4de0-80ca-e727869cc031">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [7]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1">#putting onehotencoder and LinearRegression in a pipeline</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">make_pipeline</span><span class="p">(</span>
    <span class="n">OneHotEncoder</span><span class="p">(</span><span class="n">use_cat_names</span><span class="o">=</span><span class="kc">True</span><span class="p">),</span>
    <span class="n">Ridge</span><span class="p">()</span>
<span class="p">)</span>
<span class="n">model</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr" tabindex="0">
<pre>
<span class="ansi-red-fg">---------------------------------------------------------------------------</span>
<span class="ansi-red-fg">NameError</span>                                 Traceback (most recent call last)
Cell <span class="ansi-green-fg">In[7], line 6</span>
<span class="ansi-green-intense-fg ansi-bold">      1</span> <span style="color: rgb(95,135,135)">#putting onehotencoder and LinearRegression in a pipeline</span>
<span class="ansi-green-intense-fg ansi-bold">      2</span> model <span style="color: rgb(98,98,98)">=</span> make_pipeline(
<span class="ansi-green-intense-fg ansi-bold">      3</span>     OneHotEncoder(use_cat_names<span style="color: rgb(98,98,98)">=</span><span class="ansi-bold" style="color: rgb(0,135,0)">True</span>),
<span class="ansi-green-intense-fg ansi-bold">      4</span>     Ridge()
<span class="ansi-green-intense-fg ansi-bold">      5</span> )
<span class="ansi-green-fg">----&gt; 6</span> model<span style="color: rgb(98,98,98)">.</span>fit(<span class="ansi-yellow-bg">X_train</span>, y_train)

<span class="ansi-red-fg">NameError</span>: name 'X_train' is not defined</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=432b2c22-9c54-4326-84a7-0f34d99ff193">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="Evaluate">Evaluate<a class="anchor-link" href="#Evaluate">¶</a></h2>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=157be0ad-80c4-4b2a-9b44-60ffd2dd9c84">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><strong>Task 2.5.10</strong></p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=d71a31f5-3f69-4c4f-9541-62d9a9e0e2c4">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<div class="alert alert-block alert-info">
<b>Tip:</b> Make sure the <code>X_train</code> you used to train your model has the same column order as <code>X_test</code>. Otherwise, it may hurt your model's performance.
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=9fcb2d73-9c22-4e0c-b6d0-02318981c3d0">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [16]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">X_test</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">"data/mexico-city-test-features.csv"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">X_test</span><span class="o">.</span><span class="n">info</span><span class="p">())</span>
<span class="n">X_test</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 1041 entries, 0 to 1040
Data columns (total 4 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   surface_covered_in_m2  1041 non-null   float64
 1   lat                    986 non-null    float64
 2   lon                    986 non-null    float64
 3   borough                1041 non-null   object 
dtypes: float64(3), object(1)
memory usage: 32.7+ KB
None
</pre>
</div>
</div>
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[16]:</div>
<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html" tabindex="0">
<div>
<style scoped="">
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
<thead>
<tr style="text-align: right;">
<th></th>
<th>surface_covered_in_m2</th>
<th>lat</th>
<th>lon</th>
<th>borough</th>
</tr>
</thead>
<tbody>
<tr>
<th>0</th>
<td>60.0</td>
<td>19.493185</td>
<td>-99.205755</td>
<td>Azcapotzalco</td>
</tr>
<tr>
<th>1</th>
<td>55.0</td>
<td>19.307247</td>
<td>-99.166700</td>
<td>Coyoacán</td>
</tr>
<tr>
<th>2</th>
<td>50.0</td>
<td>19.363469</td>
<td>-99.010141</td>
<td>Iztapalapa</td>
</tr>
<tr>
<th>3</th>
<td>60.0</td>
<td>19.474655</td>
<td>-99.189277</td>
<td>Azcapotzalco</td>
</tr>
<tr>
<th>4</th>
<td>74.0</td>
<td>19.394628</td>
<td>-99.143842</td>
<td>Benito Juárez</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=a7dfeb49-87ba-4eac-9502-b2851a8f3da9">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><strong>Task 2.5.11</strong></p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=c6d8cf9a-2ead-4f8a-af58-b35a3cde70de">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [22]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">y_test_pred</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">))</span>

<span class="nb">print</span><span class="p">(</span><span class="n">y_test_pred</span><span class="o">.</span><span class="n">head</span><span class="p">())</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>0    53546.903203
1    53180.932704
2    34283.733769
3    53496.942605
4    68740.812424
dtype: float64
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=61a510f1-d69d-40ba-838d-208d1cda2275">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Communicate-Results">Communicate Results<a class="anchor-link" href="#Communicate-Results">¶</a></h1>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=087e1df2-8025-4f95-b3b0-3071ff4aebd3">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><strong>Task 2.5.12</strong></p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=8c52a764-6041-4765-bf99-5c330d567e5e">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">coefficients</span> <span class="o">=</span> <span class="o">...</span>
<span class="n">features</span> <span class="o">=</span> <span class="o">...</span>
<span class="n">feat_imp</span> <span class="o">=</span> <span class="o">...</span>
<span class="n">feat_imp</span>
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=34eab663-5a3d-4e33-afef-7871c8023c21">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><strong>Task 2.5.13</strong></p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=647012e4-15de-4efc-bd04-397b43ea7e80">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>

<span class="c1"># Create the horizontal bar plot on the axes object</span>
<span class="n">feat_imp</span><span class="o">...</span><span class="n">plot</span><span class="p">(</span><span class="o">...</span><span class="p">,</span> <span class="n">ax</span><span class="o">=</span><span class="n">ax</span><span class="p">)</span>

<span class="c1">#  Label axes </span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="o">...</span><span class="p">)</span> 
<span class="n">ax</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="o">...</span><span class="p">)</span>

<span class="c1"># Add title </span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="o">...</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell" id="cell-id=3049a42c">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<hr/>
<p>Copyright 2024 WorldQuant University. This
content is licensed solely for personal use. Redistribution or
publication of this material is strictly prohibited.</p>
</div>
</div>
</div>
</div>
</main>
</body>
<script type="application/vnd.jupyter.widget-state+json">
{"state": {}, "version_major": 2, "version_minor": 0}
</script>
</html>
