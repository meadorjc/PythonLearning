Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:18:40) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> help()

Welcome to Python 3.3!  This is the interactive help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.3/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> Canvas.tk
no Python documentation found for 'Canvas.tk'

help> tkinter.Canvas
Help on class Canvas in tkinter:

tkinter.Canvas = class Canvas(Widget, XView, YView)
 |  Canvas widget to display graphical elements like lines or text.
 |  
 |  Method resolution order:
 |      Canvas
 |      Widget
 |      BaseWidget
 |      Misc
 |      Pack
 |      Place
 |      Grid
 |      XView
 |      YView
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, master=None, cnf={}, **kw)
 |      Construct a canvas widget with the parent MASTER.
 |      
 |      Valid resource names: background, bd, bg, borderwidth, closeenough,
 |      confine, cursor, height, highlightbackground, highlightcolor,
 |      highlightthickness, insertbackground, insertborderwidth,
 |      insertofftime, insertontime, insertwidth, offset, relief,
 |      scrollregion, selectbackground, selectborderwidth, selectforeground,
 |      state, takefocus, width, xscrollcommand, xscrollincrement,
 |      yscrollcommand, yscrollincrement.
 |  
 |  addtag(self, *args)
 |      Internal function.
 |  
 |  addtag_above(self, newtag, tagOrId)
 |      Add tag NEWTAG to all items above TAGORID.
 |  
 |  addtag_all(self, newtag)
 |      Add tag NEWTAG to all items.
 |  
 |  addtag_below(self, newtag, tagOrId)
 |      Add tag NEWTAG to all items below TAGORID.
 |  
 |  addtag_closest(self, newtag, x, y, halo=None, start=None)
 |      Add tag NEWTAG to item which is closest to pixel at X, Y.
 |      If several match take the top-most.
 |      All items closer than HALO are considered overlapping (all are
 |      closests). If START is specified the next below this tag is taken.
 |  
 |  addtag_enclosed(self, newtag, x1, y1, x2, y2)
 |      Add tag NEWTAG to all items in the rectangle defined
 |      by X1,Y1,X2,Y2.
 |  
 |  addtag_overlapping(self, newtag, x1, y1, x2, y2)
 |      Add tag NEWTAG to all items which overlap the rectangle
 |      defined by X1,Y1,X2,Y2.
 |  
 |  addtag_withtag(self, newtag, tagOrId)
 |      Add tag NEWTAG to all items with TAGORID.
 |  
 |  bbox(self, *args)
 |      Return a tuple of X1,Y1,X2,Y2 coordinates for a rectangle
 |      which encloses all items with tags specified as arguments.
 |  
 |  canvasx(self, screenx, gridspacing=None)
 |      Return the canvas x coordinate of pixel position SCREENX rounded
 |      to nearest multiple of GRIDSPACING units.
 |  
 |  canvasy(self, screeny, gridspacing=None)
 |      Return the canvas y coordinate of pixel position SCREENY rounded
 |      to nearest multiple of GRIDSPACING units.
 |  
 |  coords(self, *args)
 |      Return a list of coordinates for the item given in ARGS.
 |  
 |  create_arc(self, *args, **kw)
 |      Create arc shaped region with coordinates x1,y1,x2,y2.
 |  
 |  create_bitmap(self, *args, **kw)
 |      Create bitmap with coordinates x1,y1.
 |  
 |  create_image(self, *args, **kw)
 |      Create image item with coordinates x1,y1.
 |  
 |  create_line(self, *args, **kw)
 |      Create line with coordinates x1,y1,...,xn,yn.
 |  
 |  create_oval(self, *args, **kw)
 |      Create oval with coordinates x1,y1,x2,y2.
 |  
 |  create_polygon(self, *args, **kw)
 |      Create polygon with coordinates x1,y1,...,xn,yn.
 |  
 |  create_rectangle(self, *args, **kw)
 |      Create rectangle with coordinates x1,y1,x2,y2.
 |  
 |  create_text(self, *args, **kw)
 |      Create text with coordinates x1,y1.
 |  
 |  create_window(self, *args, **kw)
 |      Create window with coordinates x1,y1,x2,y2.
 |  
 |  dchars(self, *args)
 |      Delete characters of text items identified by tag or id in ARGS (possibly
 |      several times) from FIRST to LAST character (including).
 |  
 |  delete(self, *args)
 |      Delete items identified by all tag or ids contained in ARGS.
 |  
 |  dtag(self, *args)
 |      Delete tag or id given as last arguments in ARGS from items
 |      identified by first argument in ARGS.
 |  
 |  find(self, *args)
 |      Internal function.
 |  
 |  find_above(self, tagOrId)
 |      Return items above TAGORID.
 |  
 |  find_all(self)
 |      Return all items.
 |  
 |  find_below(self, tagOrId)
 |      Return all items below TAGORID.
 |  
 |  find_closest(self, x, y, halo=None, start=None)
 |      Return item which is closest to pixel at X, Y.
 |      If several match take the top-most.
 |      All items closer than HALO are considered overlapping (all are
 |      closests). If START is specified the next below this tag is taken.
 |  
 |  find_enclosed(self, x1, y1, x2, y2)
 |      Return all items in rectangle defined
 |      by X1,Y1,X2,Y2.
 |  
 |  find_overlapping(self, x1, y1, x2, y2)
 |      Return all items which overlap the rectangle
 |      defined by X1,Y1,X2,Y2.
 |  
 |  find_withtag(self, tagOrId)
 |      Return all items with TAGORID.
 |  
 |  focus(self, *args)
 |      Set focus to the first item specified in ARGS.
 |  
 |  gettags(self, *args)
 |      Return tags associated with the first item specified in ARGS.
 |  
 |  icursor(self, *args)
 |      Set cursor at position POS in the item identified by TAGORID.
 |      In ARGS TAGORID must be first.
 |  
 |  index(self, *args)
 |      Return position of cursor as integer in item specified in ARGS.
 |  
 |  insert(self, *args)
 |      Insert TEXT in item TAGORID at position POS. ARGS must
 |      be TAGORID POS TEXT.
 |  
 |  itemcget(self, tagOrId, option)
 |      Return the resource value for an OPTION for item TAGORID.
 |  
 |  itemconfig = itemconfigure(self, tagOrId, cnf=None, **kw)
 |  
 |  itemconfigure(self, tagOrId, cnf=None, **kw)
 |      Configure resources of an item TAGORID.
 |      
 |      The values for resources are specified as keyword
 |      arguments. To get an overview about
 |      the allowed keyword arguments call the method without arguments.
 |  
 |  lift = tag_raise(self, *args)
 |  
 |  lower = tag_lower(self, *args)
 |  
 |  move(self, *args)
 |      Move an item TAGORID given in ARGS.
 |  
 |  postscript(self, cnf={}, **kw)
 |      Print the contents of the canvas to a postscript
 |      file. Valid options: colormap, colormode, file, fontmap,
 |      height, pageanchor, pageheight, pagewidth, pagex, pagey,
 |      rotate, witdh, x, y.
 |  
 |  scale(self, *args)
 |      Scale item TAGORID with XORIGIN, YORIGIN, XSCALE, YSCALE.
 |  
 |  scan_dragto(self, x, y, gain=10)
 |      Adjust the view of the canvas to GAIN times the
 |      difference between X and Y and the coordinates given in
 |      scan_mark.
 |  
 |  scan_mark(self, x, y)
 |      Remember the current X, Y coordinates.
 |  
 |  select_adjust(self, tagOrId, index)
 |      Adjust the end of the selection near the cursor of an item TAGORID to index.
 |  
 |  select_clear(self)
 |      Clear the selection if it is in this widget.
 |  
 |  select_from(self, tagOrId, index)
 |      Set the fixed end of a selection in item TAGORID to INDEX.
 |  
 |  select_item(self)
 |      Return the item which has the selection.
 |  
 |  select_to(self, tagOrId, index)
 |      Set the variable end of a selection in item TAGORID to INDEX.
 |  
 |  tag_bind(self, tagOrId, sequence=None, func=None, add=None)
 |      Bind to all items with TAGORID at event SEQUENCE a call to function FUNC.
 |      
 |      An additional boolean parameter ADD specifies whether FUNC will be
 |      called additionally to the other bound function or whether it will
 |      replace the previous function. See bind for the return value.
 |  
 |  tag_lower(self, *args)
 |      Lower an item TAGORID given in ARGS
 |      (optional below another item).
 |  
 |  tag_raise(self, *args)
 |      Raise an item TAGORID given in ARGS
 |      (optional above another item).
 |  
 |  tag_unbind(self, tagOrId, sequence, funcid=None)
 |      Unbind for all items with TAGORID for event SEQUENCE  the
 |      function identified with FUNCID.
 |  
 |  tkraise = tag_raise(self, *args)
 |  
 |  type(self, tagOrId)
 |      Return the type of the item TAGORID.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from BaseWidget:
 |  
 |  destroy(self)
 |      Destroy this and all descendants widgets.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Misc:
 |  
 |  __getitem__ = cget(self, key)
 |      Return the resource value for a KEY given as string.
 |  
 |  __setitem__(self, key, value)
 |  
 |  __str__(self)
 |      Return the window path name of this widget.
 |  
 |  after(self, ms, func=None, *args)
 |      Call function once after given time.
 |      
 |      MS specifies the time in milliseconds. FUNC gives the
 |      function which shall be called. Additional parameters
 |      are given as parameters to the function call.  Return
 |      identifier to cancel scheduling with after_cancel.
 |  
 |  after_cancel(self, id)
 |      Cancel scheduling of function identified with ID.
 |      
 |      Identifier returned by after or after_idle must be
 |      given as first parameter.
 |  
 |  after_idle(self, func, *args)
 |      Call FUNC once if the Tcl main loop has no event to
 |      process.
 |      
 |      Return an identifier to cancel the scheduling with
 |      after_cancel.
 |  
 |  anchor = grid_anchor(self, anchor=None)
 |      The anchor value controls how to place the grid within the
 |      master when no row/column has any weight.
 |      
 |      The default anchor is nw.
 |  
 |  bell(self, displayof=0)
 |      Ring a display's bell.
 |  
 |  bind(self, sequence=None, func=None, add=None)
 |      Bind to this widget at event SEQUENCE a call to function FUNC.
 |      
 |      SEQUENCE is a string of concatenated event
 |      patterns. An event pattern is of the form
 |      <MODIFIER-MODIFIER-TYPE-DETAIL> where MODIFIER is one
 |      of Control, Mod2, M2, Shift, Mod3, M3, Lock, Mod4, M4,
 |      Button1, B1, Mod5, M5 Button2, B2, Meta, M, Button3,
 |      B3, Alt, Button4, B4, Double, Button5, B5 Triple,
 |      Mod1, M1. TYPE is one of Activate, Enter, Map,
 |      ButtonPress, Button, Expose, Motion, ButtonRelease
 |      FocusIn, MouseWheel, Circulate, FocusOut, Property,
 |      Colormap, Gravity Reparent, Configure, KeyPress, Key,
 |      Unmap, Deactivate, KeyRelease Visibility, Destroy,
 |      Leave and DETAIL is the button number for ButtonPress,
 |      ButtonRelease and DETAIL is the Keysym for KeyPress and
 |      KeyRelease. Examples are
 |      <Control-Button-1> for pressing Control and mouse button 1 or
 |      <Alt-A> for pressing A and the Alt key (KeyPress can be omitted).
 |      An event pattern can also be a virtual event of the form
 |      <<AString>> where AString can be arbitrary. This
 |      event can be generated by event_generate.
 |      If events are concatenated they must appear shortly
 |      after each other.
 |      
 |      FUNC will be called if the event sequence occurs with an
 |      instance of Event as argument. If the return value of FUNC is
 |      "break" no further bound function is invoked.
 |      
 |      An additional boolean parameter ADD specifies whether FUNC will
 |      be called additionally to the other bound function or whether
 |      it will replace the previous function.
 |      
 |      Bind will return an identifier to allow deletion of the bound function with
 |      unbind without memory leak.
 |      
 |      If FUNC or SEQUENCE is omitted the bound function or list
 |      of bound events are returned.
 |  
 |  bind_all(self, sequence=None, func=None, add=None)
 |      Bind to all widgets at an event SEQUENCE a call to function FUNC.
 |      An additional boolean parameter ADD specifies whether FUNC will
 |      be called additionally to the other bound function or whether
 |      it will replace the previous function. See bind for the return value.
 |  
 |  bind_class(self, className, sequence=None, func=None, add=None)
 |      Bind to widgets with bindtag CLASSNAME at event
 |      SEQUENCE a call of function FUNC. An additional
 |      boolean parameter ADD specifies whether FUNC will be
 |      called additionally to the other bound function or
 |      whether it will replace the previous function. See bind for
 |      the return value.
 |  
 |  bindtags(self, tagList=None)
 |      Set or get the list of bindtags for this widget.
 |      
 |      With no argument return the list of all bindtags associated with
 |      this widget. With a list of strings as argument the bindtags are
 |      set to this list. The bindtags determine in which order events are
 |      processed (see bind).
 |  
 |  cget(self, key)
 |      Return the resource value for a KEY given as string.
 |  
 |  clipboard_append(self, string, **kw)
 |      Append STRING to the Tk clipboard.
 |      
 |      A widget specified at the optional displayof keyword
 |      argument specifies the target display. The clipboard
 |      can be retrieved with selection_get.
 |  
 |  clipboard_clear(self, **kw)
 |      Clear the data in the Tk clipboard.
 |      
 |      A widget specified for the optional displayof keyword
 |      argument specifies the target display.
 |  
 |  clipboard_get(self, **kw)
 |      Retrieve data from the clipboard on window's display.
 |      
 |      The window keyword defaults to the root window of the Tkinter
 |      application.
 |      
 |      The type keyword specifies the form in which the data is
 |      to be returned and should be an atom name such as STRING
 |      or FILE_NAME.  Type defaults to STRING, except on X11, where the default
 |      is to try UTF8_STRING and fall back to STRING.
 |      
 |      This command is equivalent to:
 |      
 |      selection_get(CLIPBOARD)
 |  
 |  colormodel(self, value=None)
 |      Useless. Not implemented in Tk.
 |  
 |  columnconfigure = grid_columnconfigure(self, index, cnf={}, **kw)
 |      Configure column INDEX of a grid.
 |      
 |      Valid resources are minsize (minimum size of the column),
 |      weight (how much does additional space propagate to this column)
 |      and pad (how much space to let additionally).
 |  
 |  config = configure(self, cnf=None, **kw)
 |      Configure resources of a widget.
 |      
 |      The values for resources are specified as keyword
 |      arguments. To get an overview about
 |      the allowed keyword arguments call the method keys.
 |  
 |  configure(self, cnf=None, **kw)
 |      Configure resources of a widget.
 |      
 |      The values for resources are specified as keyword
 |      arguments. To get an overview about
 |      the allowed keyword arguments call the method keys.
 |  
 |  deletecommand(self, name)
 |      Internal function.
 |      
 |      Delete the Tcl command provided in NAME.
 |  
 |  event_add(self, virtual, *sequences)
 |      Bind a virtual event VIRTUAL (of the form <<Name>>)
 |      to an event SEQUENCE such that the virtual event is triggered
 |      whenever SEQUENCE occurs.
 |  
 |  event_delete(self, virtual, *sequences)
 |      Unbind a virtual event VIRTUAL from SEQUENCE.
 |  
 |  event_generate(self, sequence, **kw)
 |      Generate an event SEQUENCE. Additional
 |      keyword arguments specify parameter of the event
 |      (e.g. x, y, rootx, rooty).
 |  
 |  event_info(self, virtual=None)
 |      Return a list of all virtual events or the information
 |      about the SEQUENCE bound to the virtual event VIRTUAL.
 |  
 |  focus_displayof(self)
 |      Return the widget which has currently the focus on the
 |      display where this widget is located.
 |      
 |      Return None if the application does not have the focus.
 |  
 |  focus_force(self)
 |      Direct input focus to this widget even if the
 |      application does not have the focus. Use with
 |      caution!
 |  
 |  focus_get(self)
 |      Return the widget which has currently the focus in the
 |      application.
 |      
 |      Use focus_displayof to allow working with several
 |      displays. Return None if application does not have
 |      the focus.
 |  
 |  focus_lastfor(self)
 |      Return the widget which would have the focus if top level
 |      for this widget gets the focus from the window manager.
 |  
 |  focus_set(self)
 |      Direct input focus to this widget.
 |      
 |      If the application currently does not have the focus
 |      this widget will get the focus if the application gets
 |      the focus through the window manager.
 |  
 |  getboolean(self, s)
 |      Return a boolean value for Tcl boolean values true and false given as parameter.
 |  
 |  getvar(self, name='PY_VAR')
 |      Return value of Tcl variable NAME.
 |  
 |  grab_current(self)
 |      Return widget which has currently the grab in this application
 |      or None.
 |  
 |  grab_release(self)
 |      Release grab for this widget if currently set.
 |  
 |  grab_set(self)
 |      Set grab for this widget.
 |      
 |      A grab directs all events to this and descendant
 |      widgets in the application.
 |  
 |  grab_set_global(self)
 |      Set global grab for this widget.
 |      
 |      A global grab directs all events to this and
 |      descendant widgets on the display. Use with caution -
 |      other applications do not get events anymore.
 |  
 |  grab_status(self)
 |      Return None, "local" or "global" if this widget has
 |      no, a local or a global grab.
 |  
 |  grid_anchor(self, anchor=None)
 |      The anchor value controls how to place the grid within the
 |      master when no row/column has any weight.
 |      
 |      The default anchor is nw.
 |  
 |  grid_bbox(self, column=None, row=None, col2=None, row2=None)
 |      Return a tuple of integer coordinates for the bounding
 |      box of this widget controlled by the geometry manager grid.
 |      
 |      If COLUMN, ROW is given the bounding box applies from
 |      the cell with row and column 0 to the specified
 |      cell. If COL2 and ROW2 are given the bounding box
 |      starts at that cell.
 |      
 |      The returned integers specify the offset of the upper left
 |      corner in the master widget and the width and height.
 |  
 |  grid_columnconfigure(self, index, cnf={}, **kw)
 |      Configure column INDEX of a grid.
 |      
 |      Valid resources are minsize (minimum size of the column),
 |      weight (how much does additional space propagate to this column)
 |      and pad (how much space to let additionally).
 |  
 |  grid_location(self, x, y)
 |      Return a tuple of column and row which identify the cell
 |      at which the pixel at position X and Y inside the master
 |      widget is located.
 |  
 |  grid_propagate(self, flag=['_noarg_'])
 |      Set or get the status for propagation of geometry information.
 |      
 |      A boolean argument specifies whether the geometry information
 |      of the slaves will determine the size of this widget. If no argument
 |      is given, the current setting will be returned.
 |  
 |  grid_rowconfigure(self, index, cnf={}, **kw)
 |      Configure row INDEX of a grid.
 |      
 |      Valid resources are minsize (minimum size of the row),
 |      weight (how much does additional space propagate to this row)
 |      and pad (how much space to let additionally).
 |  
 |  grid_size(self)
 |      Return a tuple of the number of column and rows in the grid.
 |  
 |  grid_slaves(self, row=None, column=None)
 |      Return a list of all slaves of this widget
 |      in its packing order.
 |  
 |  image_names(self)
 |      Return a list of all existing image names.
 |  
 |  image_types(self)
 |      Return a list of all available image types (e.g. phote bitmap).
 |  
 |  keys(self)
 |      Return a list of all resource names of this widget.
 |  
 |  mainloop(self, n=0)
 |      Call the mainloop of Tk.
 |  
 |  nametowidget(self, name)
 |      Return the Tkinter instance of a widget identified by
 |      its Tcl name NAME.
 |  
 |  option_add(self, pattern, value, priority=None)
 |      Set a VALUE (second parameter) for an option
 |      PATTERN (first parameter).
 |      
 |      An optional third parameter gives the numeric priority
 |      (defaults to 80).
 |  
 |  option_clear(self)
 |      Clear the option database.
 |      
 |      It will be reloaded if option_add is called.
 |  
 |  option_get(self, name, className)
 |      Return the value for an option NAME for this widget
 |      with CLASSNAME.
 |      
 |      Values with higher priority override lower values.
 |  
 |  option_readfile(self, fileName, priority=None)
 |      Read file FILENAME into the option database.
 |      
 |      An optional second parameter gives the numeric
 |      priority.
 |  
 |  pack_propagate(self, flag=['_noarg_'])
 |      Set or get the status for propagation of geometry information.
 |      
 |      A boolean argument specifies whether the geometry information
 |      of the slaves will determine the size of this widget. If no argument
 |      is given the current setting will be returned.
 |  
 |  pack_slaves(self)
 |      Return a list of all slaves of this widget
 |      in its packing order.
 |  
 |  place_slaves(self)
 |      Return a list of all slaves of this widget
 |      in its packing order.
 |  
 |  propagate = pack_propagate(self, flag=['_noarg_'])
 |      Set or get the status for propagation of geometry information.
 |      
 |      A boolean argument specifies whether the geometry information
 |      of the slaves will determine the size of this widget. If no argument
 |      is given the current setting will be returned.
 |  
 |  quit(self)
 |      Quit the Tcl interpreter. All widgets will be destroyed.
 |  
 |  register = _register(self, func, subst=None, needcleanup=1)
 |      Return a newly created Tcl function. If this
 |      function is called, the Python function FUNC will
 |      be executed. An optional function SUBST can
 |      be given which will be executed before FUNC.
 |  
 |  rowconfigure = grid_rowconfigure(self, index, cnf={}, **kw)
 |      Configure row INDEX of a grid.
 |      
 |      Valid resources are minsize (minimum size of the row),
 |      weight (how much does additional space propagate to this row)
 |      and pad (how much space to let additionally).
 |  
 |  selection_clear(self, **kw)
 |      Clear the current X selection.
 |  
 |  selection_get(self, **kw)
 |      Return the contents of the current X selection.
 |      
 |      A keyword parameter selection specifies the name of
 |      the selection and defaults to PRIMARY.  A keyword
 |      parameter displayof specifies a widget on the display
 |      to use. A keyword parameter type specifies the form of data to be
 |      fetched, defaulting to STRING except on X11, where UTF8_STRING is tried
 |      before STRING.
 |  
 |  selection_handle(self, command, **kw)
 |      Specify a function COMMAND to call if the X
 |      selection owned by this widget is queried by another
 |      application.
 |      
 |      This function must return the contents of the
 |      selection. The function will be called with the
 |      arguments OFFSET and LENGTH which allows the chunking
 |      of very long selections. The following keyword
 |      parameters can be provided:
 |      selection - name of the selection (default PRIMARY),
 |      type - type of the selection (e.g. STRING, FILE_NAME).
 |  
 |  selection_own(self, **kw)
 |      Become owner of X selection.
 |      
 |      A keyword parameter selection specifies the name of
 |      the selection (default PRIMARY).
 |  
 |  selection_own_get(self, **kw)
 |      Return owner of X selection.
 |      
 |      The following keyword parameter can
 |      be provided:
 |      selection - name of the selection (default PRIMARY),
 |      type - type of the selection (e.g. STRING, FILE_NAME).
 |  
 |  send(self, interp, cmd, *args)
 |      Send Tcl command CMD to different interpreter INTERP to be executed.
 |  
 |  setvar(self, name='PY_VAR', value='1')
 |      Set Tcl variable NAME to VALUE.
 |  
 |  size = grid_size(self)
 |      Return a tuple of the number of column and rows in the grid.
 |  
 |  slaves = pack_slaves(self)
 |      Return a list of all slaves of this widget
 |      in its packing order.
 |  
 |  tk_bisque(self)
 |      Change the color scheme to light brown as used in Tk 3.6 and before.
 |  
 |  tk_focusFollowsMouse(self)
 |      The widget under mouse will get automatically focus. Can not
 |      be disabled easily.
 |  
 |  tk_focusNext(self)
 |      Return the next widget in the focus order which follows
 |      widget which has currently the focus.
 |      
 |      The focus order first goes to the next child, then to
 |      the children of the child recursively and then to the
 |      next sibling which is higher in the stacking order.  A
 |      widget is omitted if it has the takefocus resource set
 |      to 0.
 |  
 |  tk_focusPrev(self)
 |      Return previous widget in the focus order. See tk_focusNext for details.
 |  
 |  tk_menuBar(self, *args)
 |      Do not use. Needed in Tk 3.6 and earlier.
 |  
 |  tk_setPalette(self, *args, **kw)
 |      Set a new color scheme for all widget elements.
 |      
 |      A single color as argument will cause that all colors of Tk
 |      widget elements are derived from this.
 |      Alternatively several keyword parameters and its associated
 |      colors can be given. The following keywords are valid:
 |      activeBackground, foreground, selectColor,
 |      activeForeground, highlightBackground, selectBackground,
 |      background, highlightColor, selectForeground,
 |      disabledForeground, insertBackground, troughColor.
 |  
 |  tk_strictMotif(self, boolean=None)
 |      Set Tcl internal variable, whether the look and feel
 |      should adhere to Motif.
 |      
 |      A parameter of 1 means adhere to Motif (e.g. no color
 |      change if mouse passes over slider).
 |      Returns the set value.
 |  
 |  unbind(self, sequence, funcid=None)
 |      Unbind for this widget for event SEQUENCE  the
 |      function identified with FUNCID.
 |  
 |  unbind_all(self, sequence)
 |      Unbind for all widgets for event SEQUENCE all functions.
 |  
 |  unbind_class(self, className, sequence)
 |      Unbind for a all widgets with bindtag CLASSNAME for event SEQUENCE
 |      all functions.
 |  
 |  update(self)
 |      Enter event loop until all pending events have been processed by Tcl.
 |  
 |  update_idletasks(self)
 |      Enter event loop until all idle callbacks have been called. This
 |      will update the display of windows but not process events caused by
 |      the user.
 |  
 |  wait_variable(self, name='PY_VAR')
 |      Wait until the variable is modified.
 |      
 |      A parameter of type IntVar, StringVar, DoubleVar or
 |      BooleanVar must be given.
 |  
 |  wait_visibility(self, window=None)
 |      Wait until the visibility of a WIDGET changes
 |      (e.g. it appears).
 |      
 |      If no parameter is given self is used.
 |  
 |  wait_window(self, window=None)
 |      Wait until a WIDGET is destroyed.
 |      
 |      If no parameter is given self is used.
 |  
 |  waitvar = wait_variable(self, name='PY_VAR')
 |      Wait until the variable is modified.
 |      
 |      A parameter of type IntVar, StringVar, DoubleVar or
 |      BooleanVar must be given.
 |  
 |  winfo_atom(self, name, displayof=0)
 |      Return integer which represents atom NAME.
 |  
 |  winfo_atomname(self, id, displayof=0)
 |      Return name of atom with identifier ID.
 |  
 |  winfo_cells(self)
 |      Return number of cells in the colormap for this widget.
 |  
 |  winfo_children(self)
 |      Return a list of all widgets which are children of this widget.
 |  
 |  winfo_class(self)
 |      Return window class name of this widget.
 |  
 |  winfo_colormapfull(self)
 |      Return true if at the last color request the colormap was full.
 |  
 |  winfo_containing(self, rootX, rootY, displayof=0)
 |      Return the widget which is at the root coordinates ROOTX, ROOTY.
 |  
 |  winfo_depth(self)
 |      Return the number of bits per pixel.
 |  
 |  winfo_exists(self)
 |      Return true if this widget exists.
 |  
 |  winfo_fpixels(self, number)
 |      Return the number of pixels for the given distance NUMBER
 |      (e.g. "3c") as float.
 |  
 |  winfo_geometry(self)
 |      Return geometry string for this widget in the form "widthxheight+X+Y".
 |  
 |  winfo_height(self)
 |      Return height of this widget.
 |  
 |  winfo_id(self)
 |      Return identifier ID for this widget.
 |  
 |  winfo_interps(self, displayof=0)
 |      Return the name of all Tcl interpreters for this display.
 |  
 |  winfo_ismapped(self)
 |      Return true if this widget is mapped.
 |  
 |  winfo_manager(self)
 |      Return the window mananger name for this widget.
 |  
 |  winfo_name(self)
 |      Return the name of this widget.
 |  
 |  winfo_parent(self)
 |      Return the name of the parent of this widget.
 |  
 |  winfo_pathname(self, id, displayof=0)
 |      Return the pathname of the widget given by ID.
 |  
 |  winfo_pixels(self, number)
 |      Rounded integer value of winfo_fpixels.
 |  
 |  winfo_pointerx(self)
 |      Return the x coordinate of the pointer on the root window.
 |  
 |  winfo_pointerxy(self)
 |      Return a tuple of x and y coordinates of the pointer on the root window.
 |  
 |  winfo_pointery(self)
 |      Return the y coordinate of the pointer on the root window.
 |  
 |  winfo_reqheight(self)
 |      Return requested height of this widget.
 |  
 |  winfo_reqwidth(self)
 |      Return requested width of this widget.
 |  
 |  winfo_rgb(self, color)
 |      Return tuple of decimal values for red, green, blue for
 |      COLOR in this widget.
 |  
 |  winfo_rootx(self)
 |      Return x coordinate of upper left corner of this widget on the
 |      root window.
 |  
 |  winfo_rooty(self)
 |      Return y coordinate of upper left corner of this widget on the
 |      root window.
 |  
 |  winfo_screen(self)
 |      Return the screen name of this widget.
 |  
 |  winfo_screencells(self)
 |      Return the number of the cells in the colormap of the screen
 |      of this widget.
 |  
 |  winfo_screendepth(self)
 |      Return the number of bits per pixel of the root window of the
 |      screen of this widget.
 |  
 |  winfo_screenheight(self)
 |      Return the number of pixels of the height of the screen of this widget
 |      in pixel.
 |  
 |  winfo_screenmmheight(self)
 |      Return the number of pixels of the height of the screen of
 |      this widget in mm.
 |  
 |  winfo_screenmmwidth(self)
 |      Return the number of pixels of the width of the screen of
 |      this widget in mm.
 |  
 |  winfo_screenvisual(self)
 |      Return one of the strings directcolor, grayscale, pseudocolor,
 |      staticcolor, staticgray, or truecolor for the default
 |      colormodel of this screen.
 |  
 |  winfo_screenwidth(self)
 |      Return the number of pixels of the width of the screen of
 |      this widget in pixel.
 |  
 |  winfo_server(self)
 |      Return information of the X-Server of the screen of this widget in
 |      the form "XmajorRminor vendor vendorVersion".
 |  
 |  winfo_toplevel(self)
 |      Return the toplevel widget of this widget.
 |  
 |  winfo_viewable(self)
 |      Return true if the widget and all its higher ancestors are mapped.
 |  
 |  winfo_visual(self)
 |      Return one of the strings directcolor, grayscale, pseudocolor,
 |      staticcolor, staticgray, or truecolor for the
 |      colormodel of this widget.
 |  
 |  winfo_visualid(self)
 |      Return the X identifier for the visual for this widget.
 |  
 |  winfo_visualsavailable(self, includeids=0)
 |      Return a list of all visuals available for the screen
 |      of this widget.
 |      
 |      Each item in the list consists of a visual name (see winfo_visual), a
 |      depth and if INCLUDEIDS=1 is given also the X identifier.
 |  
 |  winfo_vrootheight(self)
 |      Return the height of the virtual root window associated with this
 |      widget in pixels. If there is no virtual root window return the
 |      height of the screen.
 |  
 |  winfo_vrootwidth(self)
 |      Return the width of the virtual root window associated with this
 |      widget in pixel. If there is no virtual root window return the
 |      width of the screen.
 |  
 |  winfo_vrootx(self)
 |      Return the x offset of the virtual root relative to the root
 |      window of the screen of this widget.
 |  
 |  winfo_vrooty(self)
 |      Return the y offset of the virtual root relative to the root
 |      window of the screen of this widget.
 |  
 |  winfo_width(self)
 |      Return the width of this widget.
 |  
 |  winfo_x(self)
 |      Return the x coordinate of the upper left corner of this widget
 |      in the parent.
 |  
 |  winfo_y(self)
 |      Return the y coordinate of the upper left corner of this widget
 |      in the parent.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Misc:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Misc:
 |  
 |  getdouble = <class 'float'>
 |      float(x) -> floating point number
 |      
 |      Convert a string or number to a floating point number, if possible.
 |  
 |  getint = <class 'int'>
 |      int(x=0) -> integer
 |      int(x, base=10) -> integer
 |      
 |      Convert a number or string to an integer, or return 0 if no arguments
 |      are given.  If x is a number, return x.__int__().  For floating point
 |      numbers, this truncates towards zero.
 |      
 |      If x is not a number or if base is given, then x must be a string,
 |      bytes, or bytearray instance representing an integer literal in the
 |      given base.  The literal can be preceded by '+' or '-' and be surrounded
 |      by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |      Base 0 means to interpret the base from the string as an integer literal.
 |      >>> int('0b100', base=0)
 |      4
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Pack:
 |  
 |  forget = pack_forget(self)
 |      Unmap this widget and do not use it for the packing order.
 |  
 |  info = pack_info(self)
 |      Return information about the packing options
 |      for this widget.
 |  
 |  pack = pack_configure(self, cnf={}, **kw)
 |      Pack a widget in the parent widget. Use as options:
 |      after=widget - pack it after you have packed widget
 |      anchor=NSEW (or subset) - position widget according to
 |                                given direction
 |      before=widget - pack it before you will pack widget
 |      expand=bool - expand widget if parent size grows
 |      fill=NONE or X or Y or BOTH - fill widget if widget grows
 |      in=master - use master to contain this widget
 |      in_=master - see 'in' option description
 |      ipadx=amount - add internal padding in x direction
 |      ipady=amount - add internal padding in y direction
 |      padx=amount - add padding in x direction
 |      pady=amount - add padding in y direction
 |      side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.
 |  
 |  pack_configure(self, cnf={}, **kw)
 |      Pack a widget in the parent widget. Use as options:
 |      after=widget - pack it after you have packed widget
 |      anchor=NSEW (or subset) - position widget according to
 |                                given direction
 |      before=widget - pack it before you will pack widget
 |      expand=bool - expand widget if parent size grows
 |      fill=NONE or X or Y or BOTH - fill widget if widget grows
 |      in=master - use master to contain this widget
 |      in_=master - see 'in' option description
 |      ipadx=amount - add internal padding in x direction
 |      ipady=amount - add internal padding in y direction
 |      padx=amount - add padding in x direction
 |      pady=amount - add padding in y direction
 |      side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.
 |  
 |  pack_forget(self)
 |      Unmap this widget and do not use it for the packing order.
 |  
 |  pack_info(self)
 |      Return information about the packing options
 |      for this widget.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Place:
 |  
 |  place = place_configure(self, cnf={}, **kw)
 |      Place a widget in the parent widget. Use as options:
 |      in=master - master relative to which the widget is placed
 |      in_=master - see 'in' option description
 |      x=amount - locate anchor of this widget at position x of master
 |      y=amount - locate anchor of this widget at position y of master
 |      relx=amount - locate anchor of this widget between 0.0 and 1.0
 |                    relative to width of master (1.0 is right edge)
 |      rely=amount - locate anchor of this widget between 0.0 and 1.0
 |                    relative to height of master (1.0 is bottom edge)
 |      anchor=NSEW (or subset) - position anchor according to given direction
 |      width=amount - width of this widget in pixel
 |      height=amount - height of this widget in pixel
 |      relwidth=amount - width of this widget between 0.0 and 1.0
 |                        relative to width of master (1.0 is the same width
 |                        as the master)
 |      relheight=amount - height of this widget between 0.0 and 1.0
 |                         relative to height of master (1.0 is the same
 |                         height as the master)
 |      bordermode="inside" or "outside" - whether to take border width of
 |                                         master widget into account
 |  
 |  place_configure(self, cnf={}, **kw)
 |      Place a widget in the parent widget. Use as options:
 |      in=master - master relative to which the widget is placed
 |      in_=master - see 'in' option description
 |      x=amount - locate anchor of this widget at position x of master
 |      y=amount - locate anchor of this widget at position y of master
 |      relx=amount - locate anchor of this widget between 0.0 and 1.0
 |                    relative to width of master (1.0 is right edge)
 |      rely=amount - locate anchor of this widget between 0.0 and 1.0
 |                    relative to height of master (1.0 is bottom edge)
 |      anchor=NSEW (or subset) - position anchor according to given direction
 |      width=amount - width of this widget in pixel
 |      height=amount - height of this widget in pixel
 |      relwidth=amount - width of this widget between 0.0 and 1.0
 |                        relative to width of master (1.0 is the same width
 |                        as the master)
 |      relheight=amount - height of this widget between 0.0 and 1.0
 |                         relative to height of master (1.0 is the same
 |                         height as the master)
 |      bordermode="inside" or "outside" - whether to take border width of
 |                                         master widget into account
 |  
 |  place_forget(self)
 |      Unmap this widget.
 |  
 |  place_info(self)
 |      Return information about the placing options
 |      for this widget.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Grid:
 |  
 |  grid = grid_configure(self, cnf={}, **kw)
 |      Position a widget in the parent widget in a grid. Use as options:
 |      column=number - use cell identified with given column (starting with 0)
 |      columnspan=number - this widget will span several columns
 |      in=master - use master to contain this widget
 |      in_=master - see 'in' option description
 |      ipadx=amount - add internal padding in x direction
 |      ipady=amount - add internal padding in y direction
 |      padx=amount - add padding in x direction
 |      pady=amount - add padding in y direction
 |      row=number - use cell identified with given row (starting with 0)
 |      rowspan=number - this widget will span several rows
 |      sticky=NSEW - if cell is larger on which sides will this
 |                    widget stick to the cell boundary
 |  
 |  grid_configure(self, cnf={}, **kw)
 |      Position a widget in the parent widget in a grid. Use as options:
 |      column=number - use cell identified with given column (starting with 0)
 |      columnspan=number - this widget will span several columns
 |      in=master - use master to contain this widget
 |      in_=master - see 'in' option description
 |      ipadx=amount - add internal padding in x direction
 |      ipady=amount - add internal padding in y direction
 |      padx=amount - add padding in x direction
 |      pady=amount - add padding in y direction
 |      row=number - use cell identified with given row (starting with 0)
 |      rowspan=number - this widget will span several rows
 |      sticky=NSEW - if cell is larger on which sides will this
 |                    widget stick to the cell boundary
 |  
 |  grid_forget(self)
 |      Unmap this widget.
 |  
 |  grid_info(self)
 |      Return information about the options
 |      for positioning this widget in a grid.
 |  
 |  grid_remove(self)
 |      Unmap this widget but remember the grid options.
 |  
 |  location = grid_location(self, x, y)
 |      Return a tuple of column and row which identify the cell
 |      at which the pixel at position X and Y inside the master
 |      widget is located.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from XView:
 |  
 |  xview(self, *args)
 |      Query and change the horizontal position of the view.
 |  
 |  xview_moveto(self, fraction)
 |      Adjusts the view in the window so that FRACTION of the
 |      total width of the canvas is off-screen to the left.
 |  
 |  xview_scroll(self, number, what)
 |      Shift the x-view according to NUMBER which is measured in "units"
 |      or "pages" (WHAT).
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from YView:
 |  
 |  yview(self, *args)
 |      Query and change the vertical position of the view.
 |  
 |  yview_moveto(self, fraction)
 |      Adjusts the view in the window so that FRACTION of the
 |      total height of the canvas is off-screen to the top.
 |  
 |  yview_scroll(self, number, what)
 |      Shift the y-view according to NUMBER which is measured in
 |      "units" or "pages" (WHAT).

help> Tk()
no Python documentation found for 'Tk()'

help> tkinter.root
no Python documentation found for 'tkinter.root'

help> tkinter.root()
no Python documentation found for 'tkinter.root()'

help> tkinter.Tk()
no Python documentation found for 'tkinter.Tk()'

help> tkinter.Tk
Help on class Tk in tkinter:

tkinter.Tk = class Tk(Misc, Wm)
 |  Toplevel widget of Tk which represents mostly the main window
 |  of an application. It has an associated Tcl interpreter.
 |  
 |  Method resolution order:
 |      Tk
 |      Misc
 |      Wm
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __getattr__(self, attr)
 |      Delegate attribute access to the interpreter object
 |  
 |  __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None)
 |      Return a new Toplevel widget on screen SCREENNAME. A new Tcl interpreter will
 |      be created. BASENAME will be used for the identification of the profile file (see
 |      readprofile).
 |      It is constructed from sys.argv[0] without extensions if None is given. CLASSNAME
 |      is the name of the widget class.
 |  
 |  destroy(self)
 |      Destroy this and all descendants widgets. This will
 |      end the application of this Tcl interpreter.
 |  
 |  loadtk(self)
 |  
 |  readprofile(self, baseName, className)
 |      Internal function. It reads BASENAME.tcl and CLASSNAME.tcl into
 |      the Tcl Interpreter and calls exec on the contents of BASENAME.py and
 |      CLASSNAME.py if such a file exists in the home directory.
 |  
 |  report_callback_exception(self, exc, val, tb)
 |      Internal function. It reports exception on sys.stderr.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Misc:
 |  
 |  __getitem__ = cget(self, key)
 |      Return the resource value for a KEY given as string.
 |  
 |  __setitem__(self, key, value)
 |  
 |  __str__(self)
 |      Return the window path name of this widget.
 |  
 |  after(self, ms, func=None, *args)
 |      Call function once after given time.
 |      
 |      MS specifies the time in milliseconds. FUNC gives the
 |      function which shall be called. Additional parameters
 |      are given as parameters to the function call.  Return
 |      identifier to cancel scheduling with after_cancel.
 |  
 |  after_cancel(self, id)
 |      Cancel scheduling of function identified with ID.
 |      
 |      Identifier returned by after or after_idle must be
 |      given as first parameter.
 |  
 |  after_idle(self, func, *args)
 |      Call FUNC once if the Tcl main loop has no event to
 |      process.
 |      
 |      Return an identifier to cancel the scheduling with
 |      after_cancel.
 |  
 |  anchor = grid_anchor(self, anchor=None)
 |      The anchor value controls how to place the grid within the
 |      master when no row/column has any weight.
 |      
 |      The default anchor is nw.
 |  
 |  bbox = grid_bbox(self, column=None, row=None, col2=None, row2=None)
 |      Return a tuple of integer coordinates for the bounding
 |      box of this widget controlled by the geometry manager grid.
 |      
 |      If COLUMN, ROW is given the bounding box applies from
 |      the cell with row and column 0 to the specified
 |      cell. If COL2 and ROW2 are given the bounding box
 |      starts at that cell.
 |      
 |      The returned integers specify the offset of the upper left
 |      corner in the master widget and the width and height.
 |  
 |  bell(self, displayof=0)
 |      Ring a display's bell.
 |  
 |  bind(self, sequence=None, func=None, add=None)
 |      Bind to this widget at event SEQUENCE a call to function FUNC.
 |      
 |      SEQUENCE is a string of concatenated event
 |      patterns. An event pattern is of the form
 |      <MODIFIER-MODIFIER-TYPE-DETAIL> where MODIFIER is one
 |      of Control, Mod2, M2, Shift, Mod3, M3, Lock, Mod4, M4,
 |      Button1, B1, Mod5, M5 Button2, B2, Meta, M, Button3,
 |      B3, Alt, Button4, B4, Double, Button5, B5 Triple,
 |      Mod1, M1. TYPE is one of Activate, Enter, Map,
 |      ButtonPress, Button, Expose, Motion, ButtonRelease
 |      FocusIn, MouseWheel, Circulate, FocusOut, Property,
 |      Colormap, Gravity Reparent, Configure, KeyPress, Key,
 |      Unmap, Deactivate, KeyRelease Visibility, Destroy,
 |      Leave and DETAIL is the button number for ButtonPress,
 |      ButtonRelease and DETAIL is the Keysym for KeyPress and
 |      KeyRelease. Examples are
 |      <Control-Button-1> for pressing Control and mouse button 1 or
 |      <Alt-A> for pressing A and the Alt key (KeyPress can be omitted).
 |      An event pattern can also be a virtual event of the form
 |      <<AString>> where AString can be arbitrary. This
 |      event can be generated by event_generate.
 |      If events are concatenated they must appear shortly
 |      after each other.
 |      
 |      FUNC will be called if the event sequence occurs with an
 |      instance of Event as argument. If the return value of FUNC is
 |      "break" no further bound function is invoked.
 |      
 |      An additional boolean parameter ADD specifies whether FUNC will
 |      be called additionally to the other bound function or whether
 |      it will replace the previous function.
 |      
 |      Bind will return an identifier to allow deletion of the bound function with
 |      unbind without memory leak.
 |      
 |      If FUNC or SEQUENCE is omitted the bound function or list
 |      of bound events are returned.
 |  
 |  bind_all(self, sequence=None, func=None, add=None)
 |      Bind to all widgets at an event SEQUENCE a call to function FUNC.
 |      An additional boolean parameter ADD specifies whether FUNC will
 |      be called additionally to the other bound function or whether
 |      it will replace the previous function. See bind for the return value.
 |  
 |  bind_class(self, className, sequence=None, func=None, add=None)
 |      Bind to widgets with bindtag CLASSNAME at event
 |      SEQUENCE a call of function FUNC. An additional
 |      boolean parameter ADD specifies whether FUNC will be
 |      called additionally to the other bound function or
 |      whether it will replace the previous function. See bind for
 |      the return value.
 |  
 |  bindtags(self, tagList=None)
 |      Set or get the list of bindtags for this widget.
 |      
 |      With no argument return the list of all bindtags associated with
 |      this widget. With a list of strings as argument the bindtags are
 |      set to this list. The bindtags determine in which order events are
 |      processed (see bind).
 |  
 |  cget(self, key)
 |      Return the resource value for a KEY given as string.
 |  
 |  clipboard_append(self, string, **kw)
 |      Append STRING to the Tk clipboard.
 |      
 |      A widget specified at the optional displayof keyword
 |      argument specifies the target display. The clipboard
 |      can be retrieved with selection_get.
 |  
 |  clipboard_clear(self, **kw)
 |      Clear the data in the Tk clipboard.
 |      
 |      A widget specified for the optional displayof keyword
 |      argument specifies the target display.
 |  
 |  clipboard_get(self, **kw)
 |      Retrieve data from the clipboard on window's display.
 |      
 |      The window keyword defaults to the root window of the Tkinter
 |      application.
 |      
 |      The type keyword specifies the form in which the data is
 |      to be returned and should be an atom name such as STRING
 |      or FILE_NAME.  Type defaults to STRING, except on X11, where the default
 |      is to try UTF8_STRING and fall back to STRING.
 |      
 |      This command is equivalent to:
 |      
 |      selection_get(CLIPBOARD)
 |  
 |  colormodel(self, value=None)
 |      Useless. Not implemented in Tk.
 |  
 |  columnconfigure = grid_columnconfigure(self, index, cnf={}, **kw)
 |      Configure column INDEX of a grid.
 |      
 |      Valid resources are minsize (minimum size of the column),
 |      weight (how much does additional space propagate to this column)
 |      and pad (how much space to let additionally).
 |  
 |  config = configure(self, cnf=None, **kw)
 |      Configure resources of a widget.
 |      
 |      The values for resources are specified as keyword
 |      arguments. To get an overview about
 |      the allowed keyword arguments call the method keys.
 |  
 |  configure(self, cnf=None, **kw)
 |      Configure resources of a widget.
 |      
 |      The values for resources are specified as keyword
 |      arguments. To get an overview about
 |      the allowed keyword arguments call the method keys.
 |  
 |  deletecommand(self, name)
 |      Internal function.
 |      
 |      Delete the Tcl command provided in NAME.
 |  
 |  event_add(self, virtual, *sequences)
 |      Bind a virtual event VIRTUAL (of the form <<Name>>)
 |      to an event SEQUENCE such that the virtual event is triggered
 |      whenever SEQUENCE occurs.
 |  
 |  event_delete(self, virtual, *sequences)
 |      Unbind a virtual event VIRTUAL from SEQUENCE.
 |  
 |  event_generate(self, sequence, **kw)
 |      Generate an event SEQUENCE. Additional
 |      keyword arguments specify parameter of the event
 |      (e.g. x, y, rootx, rooty).
 |  
 |  event_info(self, virtual=None)
 |      Return a list of all virtual events or the information
 |      about the SEQUENCE bound to the virtual event VIRTUAL.
 |  
 |  focus = focus_set(self)
 |      Direct input focus to this widget.
 |      
 |      If the application currently does not have the focus
 |      this widget will get the focus if the application gets
 |      the focus through the window manager.
 |  
 |  focus_displayof(self)
 |      Return the widget which has currently the focus on the
 |      display where this widget is located.
 |      
 |      Return None if the application does not have the focus.
 |  
 |  focus_force(self)
 |      Direct input focus to this widget even if the
 |      application does not have the focus. Use with
 |      caution!
 |  
 |  focus_get(self)
 |      Return the widget which has currently the focus in the
 |      application.
 |      
 |      Use focus_displayof to allow working with several
 |      displays. Return None if application does not have
 |      the focus.
 |  
 |  focus_lastfor(self)
 |      Return the widget which would have the focus if top level
 |      for this widget gets the focus from the window manager.
 |  
 |  focus_set(self)
 |      Direct input focus to this widget.
 |      
 |      If the application currently does not have the focus
 |      this widget will get the focus if the application gets
 |      the focus through the window manager.
 |  
 |  getboolean(self, s)
 |      Return a boolean value for Tcl boolean values true and false given as parameter.
 |  
 |  getvar(self, name='PY_VAR')
 |      Return value of Tcl variable NAME.
 |  
 |  grab_current(self)
 |      Return widget which has currently the grab in this application
 |      or None.
 |  
 |  grab_release(self)
 |      Release grab for this widget if currently set.
 |  
 |  grab_set(self)
 |      Set grab for this widget.
 |      
 |      A grab directs all events to this and descendant
 |      widgets in the application.
 |  
 |  grab_set_global(self)
 |      Set global grab for this widget.
 |      
 |      A global grab directs all events to this and
 |      descendant widgets on the display. Use with caution -
 |      other applications do not get events anymore.
 |  
 |  grab_status(self)
 |      Return None, "local" or "global" if this widget has
 |      no, a local or a global grab.
 |  
 |  grid_anchor(self, anchor=None)
 |      The anchor value controls how to place the grid within the
 |      master when no row/column has any weight.
 |      
 |      The default anchor is nw.
 |  
 |  grid_bbox(self, column=None, row=None, col2=None, row2=None)
 |      Return a tuple of integer coordinates for the bounding
 |      box of this widget controlled by the geometry manager grid.
 |      
 |      If COLUMN, ROW is given the bounding box applies from
 |      the cell with row and column 0 to the specified
 |      cell. If COL2 and ROW2 are given the bounding box
 |      starts at that cell.
 |      
 |      The returned integers specify the offset of the upper left
 |      corner in the master widget and the width and height.
 |  
 |  grid_columnconfigure(self, index, cnf={}, **kw)
 |      Configure column INDEX of a grid.
 |      
 |      Valid resources are minsize (minimum size of the column),
 |      weight (how much does additional space propagate to this column)
 |      and pad (how much space to let additionally).
 |  
 |  grid_location(self, x, y)
 |      Return a tuple of column and row which identify the cell
 |      at which the pixel at position X and Y inside the master
 |      widget is located.
 |  
 |  grid_propagate(self, flag=['_noarg_'])
 |      Set or get the status for propagation of geometry information.
 |      
 |      A boolean argument specifies whether the geometry information
 |      of the slaves will determine the size of this widget. If no argument
 |      is given, the current setting will be returned.
 |  
 |  grid_rowconfigure(self, index, cnf={}, **kw)
 |      Configure row INDEX of a grid.
 |      
 |      Valid resources are minsize (minimum size of the row),
 |      weight (how much does additional space propagate to this row)
 |      and pad (how much space to let additionally).
 |  
 |  grid_size(self)
 |      Return a tuple of the number of column and rows in the grid.
 |  
 |  grid_slaves(self, row=None, column=None)
 |      Return a list of all slaves of this widget
 |      in its packing order.
 |  
 |  image_names(self)
 |      Return a list of all existing image names.
 |  
 |  image_types(self)
 |      Return a list of all available image types (e.g. phote bitmap).
 |  
 |  keys(self)
 |      Return a list of all resource names of this widget.
 |  
 |  lift = tkraise(self, aboveThis=None)
 |      Raise this widget in the stacking order.
 |  
 |  lower(self, belowThis=None)
 |      Lower this widget in the stacking order.
 |  
 |  mainloop(self, n=0)
 |      Call the mainloop of Tk.
 |  
 |  nametowidget(self, name)
 |      Return the Tkinter instance of a widget identified by
 |      its Tcl name NAME.
 |  
 |  option_add(self, pattern, value, priority=None)
 |      Set a VALUE (second parameter) for an option
 |      PATTERN (first parameter).
 |      
 |      An optional third parameter gives the numeric priority
 |      (defaults to 80).
 |  
 |  option_clear(self)
 |      Clear the option database.
 |      
 |      It will be reloaded if option_add is called.
 |  
 |  option_get(self, name, className)
 |      Return the value for an option NAME for this widget
 |      with CLASSNAME.
 |      
 |      Values with higher priority override lower values.
 |  
 |  option_readfile(self, fileName, priority=None)
 |      Read file FILENAME into the option database.
 |      
 |      An optional second parameter gives the numeric
 |      priority.
 |  
 |  pack_propagate(self, flag=['_noarg_'])
 |      Set or get the status for propagation of geometry information.
 |      
 |      A boolean argument specifies whether the geometry information
 |      of the slaves will determine the size of this widget. If no argument
 |      is given the current setting will be returned.
 |  
 |  pack_slaves(self)
 |      Return a list of all slaves of this widget
 |      in its packing order.
 |  
 |  place_slaves(self)
 |      Return a list of all slaves of this widget
 |      in its packing order.
 |  
 |  propagate = pack_propagate(self, flag=['_noarg_'])
 |      Set or get the status for propagation of geometry information.
 |      
 |      A boolean argument specifies whether the geometry information
 |      of the slaves will determine the size of this widget. If no argument
 |      is given the current setting will be returned.
 |  
 |  quit(self)
 |      Quit the Tcl interpreter. All widgets will be destroyed.
 |  
 |  register = _register(self, func, subst=None, needcleanup=1)
 |      Return a newly created Tcl function. If this
 |      function is called, the Python function FUNC will
 |      be executed. An optional function SUBST can
 |      be given which will be executed before FUNC.
 |  
 |  rowconfigure = grid_rowconfigure(self, index, cnf={}, **kw)
 |      Configure row INDEX of a grid.
 |      
 |      Valid resources are minsize (minimum size of the row),
 |      weight (how much does additional space propagate to this row)
 |      and pad (how much space to let additionally).
 |  
 |  selection_clear(self, **kw)
 |      Clear the current X selection.
 |  
 |  selection_get(self, **kw)
 |      Return the contents of the current X selection.
 |      
 |      A keyword parameter selection specifies the name of
 |      the selection and defaults to PRIMARY.  A keyword
 |      parameter displayof specifies a widget on the display
 |      to use. A keyword parameter type specifies the form of data to be
 |      fetched, defaulting to STRING except on X11, where UTF8_STRING is tried
 |      before STRING.
 |  
 |  selection_handle(self, command, **kw)
 |      Specify a function COMMAND to call if the X
 |      selection owned by this widget is queried by another
 |      application.
 |      
 |      This function must return the contents of the
 |      selection. The function will be called with the
 |      arguments OFFSET and LENGTH which allows the chunking
 |      of very long selections. The following keyword
 |      parameters can be provided:
 |      selection - name of the selection (default PRIMARY),
 |      type - type of the selection (e.g. STRING, FILE_NAME).
 |  
 |  selection_own(self, **kw)
 |      Become owner of X selection.
 |      
 |      A keyword parameter selection specifies the name of
 |      the selection (default PRIMARY).
 |  
 |  selection_own_get(self, **kw)
 |      Return owner of X selection.
 |      
 |      The following keyword parameter can
 |      be provided:
 |      selection - name of the selection (default PRIMARY),
 |      type - type of the selection (e.g. STRING, FILE_NAME).
 |  
 |  send(self, interp, cmd, *args)
 |      Send Tcl command CMD to different interpreter INTERP to be executed.
 |  
 |  setvar(self, name='PY_VAR', value='1')
 |      Set Tcl variable NAME to VALUE.
 |  
 |  size = grid_size(self)
 |      Return a tuple of the number of column and rows in the grid.
 |  
 |  slaves = pack_slaves(self)
 |      Return a list of all slaves of this widget
 |      in its packing order.
 |  
 |  tk_bisque(self)
 |      Change the color scheme to light brown as used in Tk 3.6 and before.
 |  
 |  tk_focusFollowsMouse(self)
 |      The widget under mouse will get automatically focus. Can not
 |      be disabled easily.
 |  
 |  tk_focusNext(self)
 |      Return the next widget in the focus order which follows
 |      widget which has currently the focus.
 |      
 |      The focus order first goes to the next child, then to
 |      the children of the child recursively and then to the
 |      next sibling which is higher in the stacking order.  A
 |      widget is omitted if it has the takefocus resource set
 |      to 0.
 |  
 |  tk_focusPrev(self)
 |      Return previous widget in the focus order. See tk_focusNext for details.
 |  
 |  tk_menuBar(self, *args)
 |      Do not use. Needed in Tk 3.6 and earlier.
 |  
 |  tk_setPalette(self, *args, **kw)
 |      Set a new color scheme for all widget elements.
 |      
 |      A single color as argument will cause that all colors of Tk
 |      widget elements are derived from this.
 |      Alternatively several keyword parameters and its associated
 |      colors can be given. The following keywords are valid:
 |      activeBackground, foreground, selectColor,
 |      activeForeground, highlightBackground, selectBackground,
 |      background, highlightColor, selectForeground,
 |      disabledForeground, insertBackground, troughColor.
 |  
 |  tk_strictMotif(self, boolean=None)
 |      Set Tcl internal variable, whether the look and feel
 |      should adhere to Motif.
 |      
 |      A parameter of 1 means adhere to Motif (e.g. no color
 |      change if mouse passes over slider).
 |      Returns the set value.
 |  
 |  tkraise(self, aboveThis=None)
 |      Raise this widget in the stacking order.
 |  
 |  unbind(self, sequence, funcid=None)
 |      Unbind for this widget for event SEQUENCE  the
 |      function identified with FUNCID.
 |  
 |  unbind_all(self, sequence)
 |      Unbind for all widgets for event SEQUENCE all functions.
 |  
 |  unbind_class(self, className, sequence)
 |      Unbind for a all widgets with bindtag CLASSNAME for event SEQUENCE
 |      all functions.
 |  
 |  update(self)
 |      Enter event loop until all pending events have been processed by Tcl.
 |  
 |  update_idletasks(self)
 |      Enter event loop until all idle callbacks have been called. This
 |      will update the display of windows but not process events caused by
 |      the user.
 |  
 |  wait_variable(self, name='PY_VAR')
 |      Wait until the variable is modified.
 |      
 |      A parameter of type IntVar, StringVar, DoubleVar or
 |      BooleanVar must be given.
 |  
 |  wait_visibility(self, window=None)
 |      Wait until the visibility of a WIDGET changes
 |      (e.g. it appears).
 |      
 |      If no parameter is given self is used.
 |  
 |  wait_window(self, window=None)
 |      Wait until a WIDGET is destroyed.
 |      
 |      If no parameter is given self is used.
 |  
 |  waitvar = wait_variable(self, name='PY_VAR')
 |      Wait until the variable is modified.
 |      
 |      A parameter of type IntVar, StringVar, DoubleVar or
 |      BooleanVar must be given.
 |  
 |  winfo_atom(self, name, displayof=0)
 |      Return integer which represents atom NAME.
 |  
 |  winfo_atomname(self, id, displayof=0)
 |      Return name of atom with identifier ID.
 |  
 |  winfo_cells(self)
 |      Return number of cells in the colormap for this widget.
 |  
 |  winfo_children(self)
 |      Return a list of all widgets which are children of this widget.
 |  
 |  winfo_class(self)
 |      Return window class name of this widget.
 |  
 |  winfo_colormapfull(self)
 |      Return true if at the last color request the colormap was full.
 |  
 |  winfo_containing(self, rootX, rootY, displayof=0)
 |      Return the widget which is at the root coordinates ROOTX, ROOTY.
 |  
 |  winfo_depth(self)
 |      Return the number of bits per pixel.
 |  
 |  winfo_exists(self)
 |      Return true if this widget exists.
 |  
 |  winfo_fpixels(self, number)
 |      Return the number of pixels for the given distance NUMBER
 |      (e.g. "3c") as float.
 |  
 |  winfo_geometry(self)
 |      Return geometry string for this widget in the form "widthxheight+X+Y".
 |  
 |  winfo_height(self)
 |      Return height of this widget.
 |  
 |  winfo_id(self)
 |      Return identifier ID for this widget.
 |  
 |  winfo_interps(self, displayof=0)
 |      Return the name of all Tcl interpreters for this display.
 |  
 |  winfo_ismapped(self)
 |      Return true if this widget is mapped.
 |  
 |  winfo_manager(self)
 |      Return the window mananger name for this widget.
 |  
 |  winfo_name(self)
 |      Return the name of this widget.
 |  
 |  winfo_parent(self)
 |      Return the name of the parent of this widget.
 |  
 |  winfo_pathname(self, id, displayof=0)
 |      Return the pathname of the widget given by ID.
 |  
 |  winfo_pixels(self, number)
 |      Rounded integer value of winfo_fpixels.
 |  
 |  winfo_pointerx(self)
 |      Return the x coordinate of the pointer on the root window.
 |  
 |  winfo_pointerxy(self)
 |      Return a tuple of x and y coordinates of the pointer on the root window.
 |  
 |  winfo_pointery(self)
 |      Return the y coordinate of the pointer on the root window.
 |  
 |  winfo_reqheight(self)
 |      Return requested height of this widget.
 |  
 |  winfo_reqwidth(self)
 |      Return requested width of this widget.
 |  
 |  winfo_rgb(self, color)
 |      Return tuple of decimal values for red, green, blue for
 |      COLOR in this widget.
 |  
 |  winfo_rootx(self)
 |      Return x coordinate of upper left corner of this widget on the
 |      root window.
 |  
 |  winfo_rooty(self)
 |      Return y coordinate of upper left corner of this widget on the
 |      root window.
 |  
 |  winfo_screen(self)
 |      Return the screen name of this widget.
 |  
 |  winfo_screencells(self)
 |      Return the number of the cells in the colormap of the screen
 |      of this widget.
 |  
 |  winfo_screendepth(self)
 |      Return the number of bits per pixel of the root window of the
 |      screen of this widget.
 |  
 |  winfo_screenheight(self)
 |      Return the number of pixels of the height of the screen of this widget
 |      in pixel.
 |  
 |  winfo_screenmmheight(self)
 |      Return the number of pixels of the height of the screen of
 |      this widget in mm.
 |  
 |  winfo_screenmmwidth(self)
 |      Return the number of pixels of the width of the screen of
 |      this widget in mm.
 |  
 |  winfo_screenvisual(self)
 |      Return one of the strings directcolor, grayscale, pseudocolor,
 |      staticcolor, staticgray, or truecolor for the default
 |      colormodel of this screen.
 |  
 |  winfo_screenwidth(self)
 |      Return the number of pixels of the width of the screen of
 |      this widget in pixel.
 |  
 |  winfo_server(self)
 |      Return information of the X-Server of the screen of this widget in
 |      the form "XmajorRminor vendor vendorVersion".
 |  
 |  winfo_toplevel(self)
 |      Return the toplevel widget of this widget.
 |  
 |  winfo_viewable(self)
 |      Return true if the widget and all its higher ancestors are mapped.
 |  
 |  winfo_visual(self)
 |      Return one of the strings directcolor, grayscale, pseudocolor,
 |      staticcolor, staticgray, or truecolor for the
 |      colormodel of this widget.
 |  
 |  winfo_visualid(self)
 |      Return the X identifier for the visual for this widget.
 |  
 |  winfo_visualsavailable(self, includeids=0)
 |      Return a list of all visuals available for the screen
 |      of this widget.
 |      
 |      Each item in the list consists of a visual name (see winfo_visual), a
 |      depth and if INCLUDEIDS=1 is given also the X identifier.
 |  
 |  winfo_vrootheight(self)
 |      Return the height of the virtual root window associated with this
 |      widget in pixels. If there is no virtual root window return the
 |      height of the screen.
 |  
 |  winfo_vrootwidth(self)
 |      Return the width of the virtual root window associated with this
 |      widget in pixel. If there is no virtual root window return the
 |      width of the screen.
 |  
 |  winfo_vrootx(self)
 |      Return the x offset of the virtual root relative to the root
 |      window of the screen of this widget.
 |  
 |  winfo_vrooty(self)
 |      Return the y offset of the virtual root relative to the root
 |      window of the screen of this widget.
 |  
 |  winfo_width(self)
 |      Return the width of this widget.
 |  
 |  winfo_x(self)
 |      Return the x coordinate of the upper left corner of this widget
 |      in the parent.
 |  
 |  winfo_y(self)
 |      Return the y coordinate of the upper left corner of this widget
 |      in the parent.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Misc:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Misc:
 |  
 |  getdouble = <class 'float'>
 |      float(x) -> floating point number
 |      
 |      Convert a string or number to a floating point number, if possible.
 |  
 |  getint = <class 'int'>
 |      int(x=0) -> integer
 |      int(x, base=10) -> integer
 |      
 |      Convert a number or string to an integer, or return 0 if no arguments
 |      are given.  If x is a number, return x.__int__().  For floating point
 |      numbers, this truncates towards zero.
 |      
 |      If x is not a number or if base is given, then x must be a string,
 |      bytes, or bytearray instance representing an integer literal in the
 |      given base.  The literal can be preceded by '+' or '-' and be surrounded
 |      by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |      Base 0 means to interpret the base from the string as an integer literal.
 |      >>> int('0b100', base=0)
 |      4
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Wm:
 |  
 |  aspect = wm_aspect(self, minNumer=None, minDenom=None, maxNumer=None, maxDenom=None)
 |      Instruct the window manager to set the aspect ratio (width/height)
 |      of this widget to be between MINNUMER/MINDENOM and MAXNUMER/MAXDENOM. Return a tuple
 |      of the actual values if no argument is given.
 |  
 |  attributes = wm_attributes(self, *args)
 |      This subcommand returns or sets platform specific attributes
 |      
 |      The first form returns a list of the platform specific flags and
 |      their values. The second form returns the value for the specific
 |      option. The third form sets one or more of the values. The values
 |      are as follows:
 |      
 |      On Windows, -disabled gets or sets whether the window is in a
 |      disabled state. -toolwindow gets or sets the style of the window
 |      to toolwindow (as defined in the MSDN). -topmost gets or sets
 |      whether this is a topmost window (displays above all other
 |      windows).
 |      
 |      On Macintosh, XXXXX
 |      
 |      On Unix, there are currently no special attribute values.
 |  
 |  client = wm_client(self, name=None)
 |      Store NAME in WM_CLIENT_MACHINE property of this widget. Return
 |      current value.
 |  
 |  colormapwindows = wm_colormapwindows(self, *wlist)
 |      Store list of window names (WLIST) into WM_COLORMAPWINDOWS property
 |      of this widget. This list contains windows whose colormaps differ from their
 |      parents. Return current list of widgets if WLIST is empty.
 |  
 |  command = wm_command(self, value=None)
 |      Store VALUE in WM_COMMAND property. It is the command
 |      which shall be used to invoke the application. Return current
 |      command if VALUE is None.
 |  
 |  deiconify = wm_deiconify(self)
 |      Deiconify this widget. If it was never mapped it will not be mapped.
 |      On Windows it will raise this widget and give it the focus.
 |  
 |  focusmodel = wm_focusmodel(self, model=None)
 |      Set focus model to MODEL. "active" means that this widget will claim
 |      the focus itself, "passive" means that the window manager shall give
 |      the focus. Return current focus model if MODEL is None.
 |  
 |  forget = wm_forget(self, window)
 |      The window will be unmappend from the screen and will no longer
 |      be managed by wm. toplevel windows will be treated like frame
 |      windows once they are no longer managed by wm, however, the menu
 |      option configuration will be remembered and the menus will return
 |      once the widget is managed again.
 |  
 |  frame = wm_frame(self)
 |      Return identifier for decorative frame of this widget if present.
 |  
 |  geometry = wm_geometry(self, newGeometry=None)
 |      Set geometry to NEWGEOMETRY of the form =widthxheight+x+y. Return
 |      current value if None is given.
 |  
 |  grid = wm_grid(self, baseWidth=None, baseHeight=None, widthInc=None, heightInc=None)
 |      Instruct the window manager that this widget shall only be
 |      resized on grid boundaries. WIDTHINC and HEIGHTINC are the width and
 |      height of a grid unit in pixels. BASEWIDTH and BASEHEIGHT are the
 |      number of grid units requested in Tk_GeometryRequest.
 |  
 |  group = wm_group(self, pathName=None)
 |      Set the group leader widgets for related widgets to PATHNAME. Return
 |      the group leader of this widget if None is given.
 |  
 |  iconbitmap = wm_iconbitmap(self, bitmap=None, default=None)
 |      Set bitmap for the iconified widget to BITMAP. Return
 |      the bitmap if None is given.
 |      
 |      Under Windows, the DEFAULT parameter can be used to set the icon
 |      for the widget and any descendents that don't have an icon set
 |      explicitly.  DEFAULT can be the relative path to a .ico file
 |      (example: root.iconbitmap(default='myicon.ico') ).  See Tk
 |      documentation for more information.
 |  
 |  iconify = wm_iconify(self)
 |      Display widget as icon.
 |  
 |  iconmask = wm_iconmask(self, bitmap=None)
 |      Set mask for the icon bitmap of this widget. Return the
 |      mask if None is given.
 |  
 |  iconname = wm_iconname(self, newName=None)
 |      Set the name of the icon for this widget. Return the name if
 |      None is given.
 |  
 |  iconphoto = wm_iconphoto(self, default=False, *args)
 |      Sets the titlebar icon for this window based on the named photo
 |      images passed through args. If default is True, this is applied to
 |      all future created toplevels as well.
 |      
 |      The data in the images is taken as a snapshot at the time of
 |      invocation. If the images are later changed, this is not reflected
 |      to the titlebar icons. Multiple images are accepted to allow
 |      different images sizes to be provided. The window manager may scale
 |      provided icons to an appropriate size.
 |      
 |      On Windows, the images are packed into a Windows icon structure.
 |      This will override an icon specified to wm_iconbitmap, and vice
 |      versa.
 |      
 |      On X, the images are arranged into the _NET_WM_ICON X property,
 |      which most modern window managers support. An icon specified by
 |      wm_iconbitmap may exist simuultaneously.
 |      
 |      On Macintosh, this currently does nothing.
 |  
 |  iconposition = wm_iconposition(self, x=None, y=None)
 |      Set the position of the icon of this widget to X and Y. Return
 |      a tuple of the current values of X and X if None is given.
 |  
 |  iconwindow = wm_iconwindow(self, pathName=None)
 |      Set widget PATHNAME to be displayed instead of icon. Return the current
 |      value if None is given.
 |  
 |  manage = wm_manage(self, widget)
 |      The widget specified will become a stand alone top-level window.
 |      The window will be decorated with the window managers title bar,
 |      etc.
 |  
 |  maxsize = wm_maxsize(self, width=None, height=None)
 |      Set max WIDTH and HEIGHT for this widget. If the window is gridded
 |      the values are given in grid units. Return the current values if None
 |      is given.
 |  
 |  minsize = wm_minsize(self, width=None, height=None)
 |      Set min WIDTH and HEIGHT for this widget. If the window is gridded
 |      the values are given in grid units. Return the current values if None
 |      is given.
 |  
 |  overrideredirect = wm_overrideredirect(self, boolean=None)
 |      Instruct the window manager to ignore this widget
 |      if BOOLEAN is given with 1. Return the current value if None
 |      is given.
 |  
 |  positionfrom = wm_positionfrom(self, who=None)
 |      Instruct the window manager that the position of this widget shall
 |      be defined by the user if WHO is "user", and by its own policy if WHO is
 |      "program".
 |  
 |  protocol = wm_protocol(self, name=None, func=None)
 |      Bind function FUNC to command NAME for this widget.
 |      Return the function bound to NAME if None is given. NAME could be
 |      e.g. "WM_SAVE_YOURSELF" or "WM_DELETE_WINDOW".
 |  
 |  resizable = wm_resizable(self, width=None, height=None)
 |      Instruct the window manager whether this width can be resized
 |      in WIDTH or HEIGHT. Both values are boolean values.
 |  
 |  sizefrom = wm_sizefrom(self, who=None)
 |      Instruct the window manager that the size of this widget shall
 |      be defined by the user if WHO is "user", and by its own policy if WHO is
 |      "program".
 |  
 |  state = wm_state(self, newstate=None)
 |      Query or set the state of this widget as one of normal, icon,
 |      iconic (see wm_iconwindow), withdrawn, or zoomed (Windows only).
 |  
 |  title = wm_title(self, string=None)
 |      Set the title of this widget.
 |  
 |  transient = wm_transient(self, master=None)
 |      Instruct the window manager that this widget is transient
 |      with regard to widget MASTER.
 |  
 |  withdraw = wm_withdraw(self)
 |      Withdraw this widget from the screen such that it is unmapped
 |      and forgotten by the window manager. Re-draw it with wm_deiconify.
 |  
 |  wm_aspect(self, minNumer=None, minDenom=None, maxNumer=None, maxDenom=None)
 |      Instruct the window manager to set the aspect ratio (width/height)
 |      of this widget to be between MINNUMER/MINDENOM and MAXNUMER/MAXDENOM. Return a tuple
 |      of the actual values if no argument is given.
 |  
 |  wm_attributes(self, *args)
 |      This subcommand returns or sets platform specific attributes
 |      
 |      The first form returns a list of the platform specific flags and
 |      their values. The second form returns the value for the specific
 |      option. The third form sets one or more of the values. The values
 |      are as follows:
 |      
 |      On Windows, -disabled gets or sets whether the window is in a
 |      disabled state. -toolwindow gets or sets the style of the window
 |      to toolwindow (as defined in the MSDN). -topmost gets or sets
 |      whether this is a topmost window (displays above all other
 |      windows).
 |      
 |      On Macintosh, XXXXX
 |      
 |      On Unix, there are currently no special attribute values.
 |  
 |  wm_client(self, name=None)
 |      Store NAME in WM_CLIENT_MACHINE property of this widget. Return
 |      current value.
 |  
 |  wm_colormapwindows(self, *wlist)
 |      Store list of window names (WLIST) into WM_COLORMAPWINDOWS property
 |      of this widget. This list contains windows whose colormaps differ from their
 |      parents. Return current list of widgets if WLIST is empty.
 |  
 |  wm_command(self, value=None)
 |      Store VALUE in WM_COMMAND property. It is the command
 |      which shall be used to invoke the application. Return current
 |      command if VALUE is None.
 |  
 |  wm_deiconify(self)
 |      Deiconify this widget. If it was never mapped it will not be mapped.
 |      On Windows it will raise this widget and give it the focus.
 |  
 |  wm_focusmodel(self, model=None)
 |      Set focus model to MODEL. "active" means that this widget will claim
 |      the focus itself, "passive" means that the window manager shall give
 |      the focus. Return current focus model if MODEL is None.
 |  
 |  wm_forget(self, window)
 |      The window will be unmappend from the screen and will no longer
 |      be managed by wm. toplevel windows will be treated like frame
 |      windows once they are no longer managed by wm, however, the menu
 |      option configuration will be remembered and the menus will return
 |      once the widget is managed again.
 |  
 |  wm_frame(self)
 |      Return identifier for decorative frame of this widget if present.
 |  
 |  wm_geometry(self, newGeometry=None)
 |      Set geometry to NEWGEOMETRY of the form =widthxheight+x+y. Return
 |      current value if None is given.
 |  
 |  wm_grid(self, baseWidth=None, baseHeight=None, widthInc=None, heightInc=None)
 |      Instruct the window manager that this widget shall only be
 |      resized on grid boundaries. WIDTHINC and HEIGHTINC are the width and
 |      height of a grid unit in pixels. BASEWIDTH and BASEHEIGHT are the
 |      number of grid units requested in Tk_GeometryRequest.
 |  
 |  wm_group(self, pathName=None)
 |      Set the group leader widgets for related widgets to PATHNAME. Return
 |      the group leader of this widget if None is given.
 |  
 |  wm_iconbitmap(self, bitmap=None, default=None)
 |      Set bitmap for the iconified widget to BITMAP. Return
 |      the bitmap if None is given.
 |      
 |      Under Windows, the DEFAULT parameter can be used to set the icon
 |      for the widget and any descendents that don't have an icon set
 |      explicitly.  DEFAULT can be the relative path to a .ico file
 |      (example: root.iconbitmap(default='myicon.ico') ).  See Tk
 |      documentation for more information.
 |  
 |  wm_iconify(self)
 |      Display widget as icon.
 |  
 |  wm_iconmask(self, bitmap=None)
 |      Set mask for the icon bitmap of this widget. Return the
 |      mask if None is given.
 |  
 |  wm_iconname(self, newName=None)
 |      Set the name of the icon for this widget. Return the name if
 |      None is given.
 |  
 |  wm_iconphoto(self, default=False, *args)
 |      Sets the titlebar icon for this window based on the named photo
 |      images passed through args. If default is True, this is applied to
 |      all future created toplevels as well.
 |      
 |      The data in the images is taken as a snapshot at the time of
 |      invocation. If the images are later changed, this is not reflected
 |      to the titlebar icons. Multiple images are accepted to allow
 |      different images sizes to be provided. The window manager may scale
 |      provided icons to an appropriate size.
 |      
 |      On Windows, the images are packed into a Windows icon structure.
 |      This will override an icon specified to wm_iconbitmap, and vice
 |      versa.
 |      
 |      On X, the images are arranged into the _NET_WM_ICON X property,
 |      which most modern window managers support. An icon specified by
 |      wm_iconbitmap may exist simuultaneously.
 |      
 |      On Macintosh, this currently does nothing.
 |  
 |  wm_iconposition(self, x=None, y=None)
 |      Set the position of the icon of this widget to X and Y. Return
 |      a tuple of the current values of X and X if None is given.
 |  
 |  wm_iconwindow(self, pathName=None)
 |      Set widget PATHNAME to be displayed instead of icon. Return the current
 |      value if None is given.
 |  
 |  wm_manage(self, widget)
 |      The widget specified will become a stand alone top-level window.
 |      The window will be decorated with the window managers title bar,
 |      etc.
 |  
 |  wm_maxsize(self, width=None, height=None)
 |      Set max WIDTH and HEIGHT for this widget. If the window is gridded
 |      the values are given in grid units. Return the current values if None
 |      is given.
 |  
 |  wm_minsize(self, width=None, height=None)
 |      Set min WIDTH and HEIGHT for this widget. If the window is gridded
 |      the values are given in grid units. Return the current values if None
 |      is given.
 |  
 |  wm_overrideredirect(self, boolean=None)
 |      Instruct the window manager to ignore this widget
 |      if BOOLEAN is given with 1. Return the current value if None
 |      is given.
 |  
 |  wm_positionfrom(self, who=None)
 |      Instruct the window manager that the position of this widget shall
 |      be defined by the user if WHO is "user", and by its own policy if WHO is
 |      "program".
 |  
 |  wm_protocol(self, name=None, func=None)
 |      Bind function FUNC to command NAME for this widget.
 |      Return the function bound to NAME if None is given. NAME could be
 |      e.g. "WM_SAVE_YOURSELF" or "WM_DELETE_WINDOW".
 |  
 |  wm_resizable(self, width=None, height=None)
 |      Instruct the window manager whether this width can be resized
 |      in WIDTH or HEIGHT. Both values are boolean values.
 |  
 |  wm_sizefrom(self, who=None)
 |      Instruct the window manager that the size of this widget shall
 |      be defined by the user if WHO is "user", and by its own policy if WHO is
 |      "program".
 |  
 |  wm_state(self, newstate=None)
 |      Query or set the state of this widget as one of normal, icon,
 |      iconic (see wm_iconwindow), withdrawn, or zoomed (Windows only).
 |  
 |  wm_title(self, string=None)
 |      Set the title of this widget.
 |  
 |  wm_transient(self, master=None)
 |      Instruct the window manager that this widget is transient
 |      with regard to widget MASTER.
 |  
 |  wm_withdraw(self)
 |      Withdraw this widget from the screen such that it is unmapped
 |      and forgotten by the window manager. Re-draw it with wm_deiconify.

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> import sys
>>> sys.path.insert(0, 'c:\\users\\compy\\documents\\github\\pythonlearning')

>>> from PeriodicCoordinateMap import *
>>> from tkinter import *

>>> 
>>> from tkinter import ttk

>>> 
>>> import zlib

>>> 
>>> from PIL import Image

>>> 
>>> import pybel

>>> root = Tk()
>>> lblfr = ttk.LabelFrame(root, text='Periodic Table', height=450, width=790)
>>> canv = Canvas(periodic_lbl_frame, height=450, width=790)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    canv = Canvas(periodic_lbl_frame, height=450, width=790)
NameError: name 'periodic_lbl_frame' is not defined
>>> canv = Canvas(lblfr, height=450, width=790)
>>> periodic_t = PhotoImage(file="Periodic_table.gif")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    periodic_t = PhotoImage(file="Periodic_table.gif")
  File "C:\Python33x86\lib\tkinter\__init__.py", line 3406, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 3362, in __init__
    self.tk.call(('image', 'create', imgtype, name,) + options)
_tkinter.TclError: couldn't open "Periodic_table.gif": no such file or directory
>>> periodic_t = PhotoImage(file="c:\\users\\compy\\documents\\github\\pythonlearning\\Periodic_table.gif")
>>> canv.create_image((635, 210), image=periodic_t)
1
>>> root.pack()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    root.pack()
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1867, in __getattr__
    return getattr(self.tk, attr)
AttributeError: 'tkapp' object has no attribute 'pack'
>>> lblfr.pack()
>>> lblfr.pack(side=LEFT, fill=BOTH, expand=1, anchor=W, padx=10, pady=10)
>>> canv.pack()
>>> canv.winfo_rootx9)
SyntaxError: invalid syntax
>>> canv.winfo_rootx()
95
>>> canv.winfo_rooty()
132
>>> canv.create_image((95, 132), image=periodic_t)
2
>>> lblfr.winfo_rootx()
93
>>> lblfr.winfo_rooty()
115
>>> canv.keys()
['background', 'bd', 'bg', 'borderwidth', 'closeenough', 'confine', 'cursor', 'height', 'highlightbackground', 'highlightcolor', 'highlightthickness', 'insertbackground', 'insertborderwidth', 'insertofftime', 'insertontime', 'insertwidth', 'offset', 'relief', 'scrollregion', 'selectbackground', 'selectborderwidth', 'selectforeground', 'state', 'takefocus', 'width', 'xscrollcommand', 'xscrollincrement', 'yscrollcommand', 'yscrollincrement']
>>> canv.configure(borderwidth=10, background='red')
>>> canv.configure(borderwidth=0, background='red')
>>> canv.configure(borderwidth=1, background='red')
>>> canv.image.keys()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    canv.image.keys()
AttributeError: 'Canvas' object has no attribute 'image'
>>> canv.children()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    canv.children()
TypeError: 'dict' object is not callable
>>> canv.children
{}
>>> canv.find_all()
(1, 2)
>>> canv.find(1)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    canv.find(1)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2352, in find
    self.tk.call((self._w, 'find') + args)) or ()
_tkinter.TclError: bad search command "1": must be above, all, below, closest, enclosed, overlapping, or withtag
>>> canv.find('1')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    canv.find('1')
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2352, in find
    self.tk.call((self._w, 'find') + args)) or ()
_tkinter.TclError: bad search command "1": must be above, all, below, closest, enclosed, overlapping, or withtag
>>> canv.find()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    canv.find()
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2352, in find
    self.tk.call((self._w, 'find') + args)) or ()
_tkinter.TclError: wrong # args: should be ".53584656.53585040 find searchCommand ?arg arg ...?"
>>> canv.winfo_rootx()
95
>>> canv.canvasx(canv.winfo_rootx())
95.0
>>> canv.canvasx(canv.winfo_rooty())
132.0
>>> canv.create_image((canv.canvasx(canv.winfo_rootx()), canv.canvasy(canv.winfo_rootx())), image=periodic_t)
3
>>> canv.create_image((canv.canvasx(canv.winfo_rootx()), canv.canvasy(canv.winfo_rootx())), image=periodic_t)
4
>>> image = canv.canvasx(canv.winfo_rootx())canv.canvasx(canv.winfo_rootx())
SyntaxError: invalid syntax
>>> image = canv.create_image((canv.canvasx(canv.winfo_rootx()), canv.canvasy(canv.winfo_rootx())), image=periodic_t)
>>> iamge
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    iamge
NameError: name 'iamge' is not defined
>>> image
5
>>> canv[5]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    canv[5]
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1267, in cget
    return self.tk.call(self._w, 'cget', '-' + key)
TypeError: Can't convert 'int' object to str implicitly
>>> canv
<tkinter.Canvas object at 0x0331A490>
>>> canv.delete()
>>> canv
<tkinter.Canvas object at 0x0331A490>
>>> canv.find_all()
(1, 2, 3, 4, 5)
>>> canv.delete(canv.find_all())
>>> canv.find_all()
(1, 2, 3, 4, 5)
>>> canv.delete(1)
>>> canv.delete(2)
>>> canv.delete(3)
>>> canv.delete(4)
>>> canv.findall()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    canv.findall()
AttributeError: 'Canvas' object has no attribute 'findall'
>>> canv.find_all()
(5,)
>>> canv.find(5)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    canv.find(5)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2352, in find
    self.tk.call((self._w, 'find') + args)) or ()
_tkinter.TclError: bad search command "5": must be above, all, below, closest, enclosed, overlapping, or withtag
>>> canv.find()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    canv.find()
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2352, in find
    self.tk.call((self._w, 'find') + args)) or ()
_tkinter.TclError: wrong # args: should be ".53584656.53585040 find searchCommand ?arg arg ...?"
>>> canv.index
<bound method Canvas.index of <tkinter.Canvas object at 0x0331A490>>
>>> canv.index()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    canv.index()
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2392, in index
    return getint(self.tk.call((self._w, 'index') + args))
_tkinter.TclError: wrong # args: should be ".53584656.53585040 index tagOrId string"
>>> canv.winfo_viewable
<bound method Canvas.winfo_viewable of <tkinter.Canvas object at 0x0331A490>>
>>> canv.winfo_viewable()
1
>>> image = canv.create_image((canv.canvasx(canv.winfo_rootx())+(450/2), canv.canvasy(canv.winfo_rootx()+(790/2))), image=periodic_t)
>>> image = canv.create_image((canv.canvasx(canv.winfo_rootx())+(790/2), canv.canvasy(canv.winfo_rootx()+(450/2))), image=periodic_t)
>>> image = canv.create_image((790/2,450/2), image=periodic_t)
>>> help()

Welcome to Python 3.3!  This is the interactive help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.3/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> tkinter.Canvas()
no Python documentation found for 'tkinter.Canvas()'

help> tkinter.Canvas
Help on class Canvas in tkinter:

tkinter.Canvas = class Canvas(Widget, XView, YView)
 |  Canvas widget to display graphical elements like lines or text.
 |  
 |  Method resolution order:
 |      Canvas
 |      Widget
 |      BaseWidget
 |      Misc
 |      Pack
 |      Place
 |      Grid
 |      XView
 |      YView
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, master=None, cnf={}, **kw)
 |      Construct a canvas widget with the parent MASTER.
 |      
 |      Valid resource names: background, bd, bg, borderwidth, closeenough,
 |      confine, cursor, height, highlightbackground, highlightcolor,
 |      highlightthickness, insertbackground, insertborderwidth,
 |      insertofftime, insertontime, insertwidth, offset, relief,
 |      scrollregion, selectbackground, selectborderwidth, selectforeground,
 |      state, takefocus, width, xscrollcommand, xscrollincrement,
 |      yscrollcommand, yscrollincrement.
 |  
 |  addtag(self, *args)
 |      Internal function.
 |  
 |  addtag_above(self, newtag, tagOrId)
 |      Add tag NEWTAG to all items above TAGORID.
 |  
 |  addtag_all(self, newtag)
 |      Add tag NEWTAG to all items.
 |  
 |  addtag_below(self, newtag, tagOrId)
 |      Add tag NEWTAG to all items below TAGORID.
 |  
 |  addtag_closest(self, newtag, x, y, halo=None, start=None)
 |      Add tag NEWTAG to item which is closest to pixel at X, Y.
 |      If several match take the top-most.
 |      All items closer than HALO are considered overlapping (all are
 |      closests). If START is specified the next below this tag is taken.
 |  
 |  addtag_enclosed(self, newtag, x1, y1, x2, y2)
 |      Add tag NEWTAG to all items in the rectangle defined
 |      by X1,Y1,X2,Y2.
 |  
 |  addtag_overlapping(self, newtag, x1, y1, x2, y2)
 |      Add tag NEWTAG to all items which overlap the rectangle
 |      defined by X1,Y1,X2,Y2.
 |  
 |  addtag_withtag(self, newtag, tagOrId)
 |      Add tag NEWTAG to all items with TAGORID.
 |  
 |  bbox(self, *args)
 |      Return a tuple of X1,Y1,X2,Y2 coordinates for a rectangle
 |      which encloses all items with tags specified as arguments.
 |  
 |  canvasx(self, screenx, gridspacing=None)
 |      Return the canvas x coordinate of pixel position SCREENX rounded
 |      to nearest multiple of GRIDSPACING units.
 |  
 |  canvasy(self, screeny, gridspacing=None)
 |      Return the canvas y coordinate of pixel position SCREENY rounded
 |      to nearest multiple of GRIDSPACING units.
 |  
 |  coords(self, *args)
 |      Return a list of coordinates for the item given in ARGS.
 |  
 |  create_arc(self, *args, **kw)
 |      Create arc shaped region with coordinates x1,y1,x2,y2.
 |  
 |  create_bitmap(self, *args, **kw)
 |      Create bitmap with coordinates x1,y1.
 |  
 |  create_image(self, *args, **kw)
 |      Create image item with coordinates x1,y1.
 |  
 |  create_line(self, *args, **kw)
 |      Create line with coordinates x1,y1,...,xn,yn.
 |  
 |  create_oval(self, *args, **kw)
 |      Create oval with coordinates x1,y1,x2,y2.
 |  
 |  create_polygon(self, *args, **kw)
 |      Create polygon with coordinates x1,y1,...,xn,yn.
 |  
 |  create_rectangle(self, *args, **kw)
 |      Create rectangle with coordinates x1,y1,x2,y2.
 |  
 |  create_text(self, *args, **kw)
 |      Create text with coordinates x1,y1.
 |  
 |  create_window(self, *args, **kw)
 |      Create window with coordinates x1,y1,x2,y2.
 |  
 |  dchars(self, *args)
 |      Delete characters of text items identified by tag or id in ARGS (possibly
 |      several times) from FIRST to LAST character (including).
 |  
 |  delete(self, *args)
 |      Delete items identified by all tag or ids contained in ARGS.
 |  
 |  dtag(self, *args)
 |      Delete tag or id given as last arguments in ARGS from items
 |      identified by first argument in ARGS.
 |  
 |  find(self, *args)
 |      Internal function.
 |  
 |  find_above(self, tagOrId)
 |      Return items above TAGORID.
 |  
 |  find_all(self)
 |      Return all items.
 |  
 |  find_below(self, tagOrId)
 |      Return all items below TAGORID.
 |  
 |  find_closest(self, x, y, halo=None, start=None)
 |      Return item which is closest to pixel at X, Y.
 |      If several match take the top-most.
 |      All items closer than HALO are considered overlapping (all are
 |      closests). If START is specified the next below this tag is taken.
 |  
 |  find_enclosed(self, x1, y1, x2, y2)
 |      Return all items in rectangle defined
 |      by X1,Y1,X2,Y2.
 |  
 |  find_overlapping(self, x1, y1, x2, y2)
 |      Return all items which overlap the rectangle
 |      defined by X1,Y1,X2,Y2.
 |  
 |  find_withtag(self, tagOrId)
 |      Return all items with TAGORID.
 |  
 |  focus(self, *args)
 |      Set focus to the first item specified in ARGS.
 |  
 |  gettags(self, *args)
 |      Return tags associated with the first item specified in ARGS.
 |  
 |  icursor(self, *args)
 |      Set cursor at position POS in the item identified by TAGORID.
 |      In ARGS TAGORID must be first.
 |  
 |  index(self, *args)
 |      Return position of cursor as integer in item specified in ARGS.
 |  
 |  insert(self, *args)
 |      Insert TEXT in item TAGORID at position POS. ARGS must
 |      be TAGORID POS TEXT.
 |  
 |  itemcget(self, tagOrId, option)
 |      Return the resource value for an OPTION for item TAGORID.
 |  
 |  itemconfig = itemconfigure(self, tagOrId, cnf=None, **kw)
 |  
 |  itemconfigure(self, tagOrId, cnf=None, **kw)
 |      Configure resources of an item TAGORID.
 |      
 |      The values for resources are specified as keyword
 |      arguments. To get an overview about
 |      the allowed keyword arguments call the method without arguments.
 |  
 |  lift = tag_raise(self, *args)
 |  
 |  lower = tag_lower(self, *args)
 |  
 |  move(self, *args)
 |      Move an item TAGORID given in ARGS.
 |  
 |  postscript(self, cnf={}, **kw)
 |      Print the contents of the canvas to a postscript
 |      file. Valid options: colormap, colormode, file, fontmap,
 |      height, pageanchor, pageheight, pagewidth, pagex, pagey,
 |      rotate, witdh, x, y.
 |  
 |  scale(self, *args)
 |      Scale item TAGORID with XORIGIN, YORIGIN, XSCALE, YSCALE.
 |  
 |  scan_dragto(self, x, y, gain=10)
 |      Adjust the view of the canvas to GAIN times the
 |      difference between X and Y and the coordinates given in
 |      scan_mark.
 |  
 |  scan_mark(self, x, y)
 |      Remember the current X, Y coordinates.
 |  
 |  select_adjust(self, tagOrId, index)
 |      Adjust the end of the selection near the cursor of an item TAGORID to index.
 |  
 |  select_clear(self)
 |      Clear the selection if it is in this widget.
 |  
 |  select_from(self, tagOrId, index)
 |      Set the fixed end of a selection in item TAGORID to INDEX.
 |  
 |  select_item(self)
 |      Return the item which has the selection.
 |  
 |  select_to(self, tagOrId, index)
 |      Set the variable end of a selection in item TAGORID to INDEX.
 |  
 |  tag_bind(self, tagOrId, sequence=None, func=None, add=None)
 |      Bind to all items with TAGORID at event SEQUENCE a call to function FUNC.
 |      
 |      An additional boolean parameter ADD specifies whether FUNC will be
 |      called additionally to the other bound function or whether it will
 |      replace the previous function. See bind for the return value.
 |  
 |  tag_lower(self, *args)
 |      Lower an item TAGORID given in ARGS
 |      (optional below another item).
 |  
 |  tag_raise(self, *args)
 |      Raise an item TAGORID given in ARGS
 |      (optional above another item).
 |  
 |  tag_unbind(self, tagOrId, sequence, funcid=None)
 |      Unbind for all items with TAGORID for event SEQUENCE  the
 |      function identified with FUNCID.
 |  
 |  tkraise = tag_raise(self, *args)
 |  
 |  type(self, tagOrId)
 |      Return the type of the item TAGORID.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from BaseWidget:
 |  
 |  destroy(self)
 |      Destroy this and all descendants widgets.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Misc:
 |  
 |  __getitem__ = cget(self, key)
 |      Return the resource value for a KEY given as string.
 |  
 |  __setitem__(self, key, value)
 |  
 |  __str__(self)
 |      Return the window path name of this widget.
 |  
 |  after(self, ms, func=None, *args)
 |      Call function once after given time.
 |      
 |      MS specifies the time in milliseconds. FUNC gives the
 |      function which shall be called. Additional parameters
 |      are given as parameters to the function call.  Return
 |      identifier to cancel scheduling with after_cancel.
 |  
 |  after_cancel(self, id)
 |      Cancel scheduling of function identified with ID.
 |      
 |      Identifier returned by after or after_idle must be
 |      given as first parameter.
 |  
 |  after_idle(self, func, *args)
 |      Call FUNC once if the Tcl main loop has no event to
 |      process.
 |      
 |      Return an identifier to cancel the scheduling with
 |      after_cancel.
 |  
 |  anchor = grid_anchor(self, anchor=None)
 |      The anchor value controls how to place the grid within the
 |      master when no row/column has any weight.
 |      
 |      The default anchor is nw.
 |  
 |  bell(self, displayof=0)
 |      Ring a display's bell.
 |  
 |  bind(self, sequence=None, func=None, add=None)
 |      Bind to this widget at event SEQUENCE a call to function FUNC.
 |      
 |      SEQUENCE is a string of concatenated event
 |      patterns. An event pattern is of the form
 |      <MODIFIER-MODIFIER-TYPE-DETAIL> where MODIFIER is one
 |      of Control, Mod2, M2, Shift, Mod3, M3, Lock, Mod4, M4,
 |      Button1, B1, Mod5, M5 Button2, B2, Meta, M, Button3,
 |      B3, Alt, Button4, B4, Double, Button5, B5 Triple,
 |      Mod1, M1. TYPE is one of Activate, Enter, Map,
 |      ButtonPress, Button, Expose, Motion, ButtonRelease
 |      FocusIn, MouseWheel, Circulate, FocusOut, Property,
 |      Colormap, Gravity Reparent, Configure, KeyPress, Key,
 |      Unmap, Deactivate, KeyRelease Visibility, Destroy,
 |      Leave and DETAIL is the button number for ButtonPress,
 |      ButtonRelease and DETAIL is the Keysym for KeyPress and
 |      KeyRelease. Examples are
 |      <Control-Button-1> for pressing Control and mouse button 1 or
 |      <Alt-A> for pressing A and the Alt key (KeyPress can be omitted).
 |      An event pattern can also be a virtual event of the form
 |      <<AString>> where AString can be arbitrary. This
 |      event can be generated by event_generate.
 |      If events are concatenated they must appear shortly
 |      after each other.
 |      
 |      FUNC will be called if the event sequence occurs with an
 |      instance of Event as argument. If the return value of FUNC is
 |      "break" no further bound function is invoked.
 |      
 |      An additional boolean parameter ADD specifies whether FUNC will
 |      be called additionally to the other bound function or whether
 |      it will replace the previous function.
 |      
 |      Bind will return an identifier to allow deletion of the bound function with
 |      unbind without memory leak.
 |      
 |      If FUNC or SEQUENCE is omitted the bound function or list
 |      of bound events are returned.
 |  
 |  bind_all(self, sequence=None, func=None, add=None)
 |      Bind to all widgets at an event SEQUENCE a call to function FUNC.
 |      An additional boolean parameter ADD specifies whether FUNC will
 |      be called additionally to the other bound function or whether
 |      it will replace the previous function. See bind for the return value.
 |  
 |  bind_class(self, className, sequence=None, func=None, add=None)
 |      Bind to widgets with bindtag CLASSNAME at event
 |      SEQUENCE a call of function FUNC. An additional
 |      boolean parameter ADD specifies whether FUNC will be
 |      called additionally to the other bound function or
 |      whether it will replace the previous function. See bind for
 |      the return value.
 |  
 |  bindtags(self, tagList=None)
 |      Set or get the list of bindtags for this widget.
 |      
 |      With no argument return the list of all bindtags associated with
 |      this widget. With a list of strings as argument the bindtags are
 |      set to this list. The bindtags determine in which order events are
 |      processed (see bind).
 |  
 |  cget(self, key)
 |      Return the resource value for a KEY given as string.
 |  
 |  clipboard_append(self, string, **kw)
 |      Append STRING to the Tk clipboard.
 |      
 |      A widget specified at the optional displayof keyword
 |      argument specifies the target display. The clipboard
 |      can be retrieved with selection_get.
 |  
 |  clipboard_clear(self, **kw)
 |      Clear the data in the Tk clipboard.
 |      
 |      A widget specified for the optional displayof keyword
 |      argument specifies the target display.
 |  
 |  clipboard_get(self, **kw)
 |      Retrieve data from the clipboard on window's display.
 |      
 |      The window keyword defaults to the root window of the Tkinter
 |      application.
 |      
 |      The type keyword specifies the form in which the data is
 |      to be returned and should be an atom name such as STRING
 |      or FILE_NAME.  Type defaults to STRING, except on X11, where the default
 |      is to try UTF8_STRING and fall back to STRING.
 |      
 |      This command is equivalent to:
 |      
 |      selection_get(CLIPBOARD)
 |  
 |  colormodel(self, value=None)
 |      Useless. Not implemented in Tk.
 |  
 |  columnconfigure = grid_columnconfigure(self, index, cnf={}, **kw)
 |      Configure column INDEX of a grid.
 |      
 |      Valid resources are minsize (minimum size of the column),
 |      weight (how much does additional space propagate to this column)
 |      and pad (how much space to let additionally).
 |  
 |  config = configure(self, cnf=None, **kw)
 |      Configure resources of a widget.
 |      
 |      The values for resources are specified as keyword
 |      arguments. To get an overview about
 |      the allowed keyword arguments call the method keys.
 |  
 |  configure(self, cnf=None, **kw)
 |      Configure resources of a widget.
 |      
 |      The values for resources are specified as keyword
 |      arguments. To get an overview about
 |      the allowed keyword arguments call the method keys.
 |  
 |  deletecommand(self, name)
 |      Internal function.
 |      
 |      Delete the Tcl command provided in NAME.
 |  
 |  event_add(self, virtual, *sequences)
 |      Bind a virtual event VIRTUAL (of the form <<Name>>)
 |      to an event SEQUENCE such that the virtual event is triggered
 |      whenever SEQUENCE occurs.
 |  
 |  event_delete(self, virtual, *sequences)
 |      Unbind a virtual event VIRTUAL from SEQUENCE.
 |  
 |  event_generate(self, sequence, **kw)
 |      Generate an event SEQUENCE. Additional
 |      keyword arguments specify parameter of the event
 |      (e.g. x, y, rootx, rooty).
 |  
 |  event_info(self, virtual=None)
 |      Return a list of all virtual events or the information
 |      about the SEQUENCE bound to the virtual event VIRTUAL.
 |  
 |  focus_displayof(self)
 |      Return the widget which has currently the focus on the
 |      display where this widget is located.
 |      
 |      Return None if the application does not have the focus.
 |  
 |  focus_force(self)
 |      Direct input focus to this widget even if the
 |      application does not have the focus. Use with
 |      caution!
 |  
 |  focus_get(self)
 |      Return the widget which has currently the focus in the
 |      application.
 |      
 |      Use focus_displayof to allow working with several
 |      displays. Return None if application does not have
 |      the focus.
 |  
 |  focus_lastfor(self)
 |      Return the widget which would have the focus if top level
 |      for this widget gets the focus from the window manager.
 |  
 |  focus_set(self)
 |      Direct input focus to this widget.
 |      
 |      If the application currently does not have the focus
 |      this widget will get the focus if the application gets
 |      the focus through the window manager.
 |  
 |  getboolean(self, s)
 |      Return a boolean value for Tcl boolean values true and false given as parameter.
 |  
 |  getvar(self, name='PY_VAR')
 |      Return value of Tcl variable NAME.
 |  
 |  grab_current(self)
 |      Return widget which has currently the grab in this application
 |      or None.
 |  
 |  grab_release(self)
 |      Release grab for this widget if currently set.
 |  
 |  grab_set(self)
 |      Set grab for this widget.
 |      
 |      A grab directs all events to this and descendant
 |      widgets in the application.
 |  
 |  grab_set_global(self)
 |      Set global grab for this widget.
 |      
 |      A global grab directs all events to this and
 |      descendant widgets on the display. Use with caution -
 |      other applications do not get events anymore.
 |  
 |  grab_status(self)
 |      Return None, "local" or "global" if this widget has
 |      no, a local or a global grab.
 |  
 |  grid_anchor(self, anchor=None)
 |      The anchor value controls how to place the grid within the
 |      master when no row/column has any weight.
 |      
 |      The default anchor is nw.
 |  
 |  grid_bbox(self, column=None, row=None, col2=None, row2=None)
 |      Return a tuple of integer coordinates for the bounding
 |      box of this widget controlled by the geometry manager grid.
 |      
 |      If COLUMN, ROW is given the bounding box applies from
 |      the cell with row and column 0 to the specified
 |      cell. If COL2 and ROW2 are given the bounding box
 |      starts at that cell.
 |      
 |      The returned integers specify the offset of the upper left
 |      corner in the master widget and the width and height.
 |  
 |  grid_columnconfigure(self, index, cnf={}, **kw)
 |      Configure column INDEX of a grid.
 |      
 |      Valid resources are minsize (minimum size of the column),
 |      weight (how much does additional space propagate to this column)
 |      and pad (how much space to let additionally).
 |  
 |  grid_location(self, x, y)
 |      Return a tuple of column and row which identify the cell
 |      at which the pixel at position X and Y inside the master
 |      widget is located.
 |  
 |  grid_propagate(self, flag=['_noarg_'])
 |      Set or get the status for propagation of geometry information.
 |      
 |      A boolean argument specifies whether the geometry information
 |      of the slaves will determine the size of this widget. If no argument
 |      is given, the current setting will be returned.
 |  
 |  grid_rowconfigure(self, index, cnf={}, **kw)
 |      Configure row INDEX of a grid.
 |      
 |      Valid resources are minsize (minimum size of the row),
 |      weight (how much does additional space propagate to this row)
 |      and pad (how much space to let additionally).
 |  
 |  grid_size(self)
 |      Return a tuple of the number of column and rows in the grid.
 |  
 |  grid_slaves(self, row=None, column=None)
 |      Return a list of all slaves of this widget
 |      in its packing order.
 |  
 |  image_names(self)
 |      Return a list of all existing image names.
 |  
 |  image_types(self)
 |      Return a list of all available image types (e.g. phote bitmap).
 |  
 |  keys(self)
 |      Return a list of all resource names of this widget.
 |  
 |  mainloop(self, n=0)
 |      Call the mainloop of Tk.
 |  
 |  nametowidget(self, name)
 |      Return the Tkinter instance of a widget identified by
 |      its Tcl name NAME.
 |  
 |  option_add(self, pattern, value, priority=None)
 |      Set a VALUE (second parameter) for an option
 |      PATTERN (first parameter).
 |      
 |      An optional third parameter gives the numeric priority
 |      (defaults to 80).
 |  
 |  option_clear(self)
 |      Clear the option database.
 |      
 |      It will be reloaded if option_add is called.
 |  
 |  option_get(self, name, className)
 |      Return the value for an option NAME for this widget
 |      with CLASSNAME.
 |      
 |      Values with higher priority override lower values.
 |  
 |  option_readfile(self, fileName, priority=None)
 |      Read file FILENAME into the option database.
 |      
 |      An optional second parameter gives the numeric
 |      priority.
 |  
 |  pack_propagate(self, flag=['_noarg_'])
 |      Set or get the status for propagation of geometry information.
 |      
 |      A boolean argument specifies whether the geometry information
 |      of the slaves will determine the size of this widget. If no argument
 |      is given the current setting will be returned.
 |  
 |  pack_slaves(self)
 |      Return a list of all slaves of this widget
 |      in its packing order.
 |  
 |  place_slaves(self)
 |      Return a list of all slaves of this widget
 |      in its packing order.
 |  
 |  propagate = pack_propagate(self, flag=['_noarg_'])
 |      Set or get the status for propagation of geometry information.
 |      
 |      A boolean argument specifies whether the geometry information
 |      of the slaves will determine the size of this widget. If no argument
 |      is given the current setting will be returned.
 |  
 |  quit(self)
 |      Quit the Tcl interpreter. All widgets will be destroyed.
 |  
 |  register = _register(self, func, subst=None, needcleanup=1)
 |      Return a newly created Tcl function. If this
 |      function is called, the Python function FUNC will
 |      be executed. An optional function SUBST can
 |      be given which will be executed before FUNC.
 |  
 |  rowconfigure = grid_rowconfigure(self, index, cnf={}, **kw)
 |      Configure row INDEX of a grid.
 |      
 |      Valid resources are minsize (minimum size of the row),
 |      weight (how much does additional space propagate to this row)
 |      and pad (how much space to let additionally).
 |  
 |  selection_clear(self, **kw)
 |      Clear the current X selection.
 |  
 |  selection_get(self, **kw)
 |      Return the contents of the current X selection.
 |      
 |      A keyword parameter selection specifies the name of
 |      the selection and defaults to PRIMARY.  A keyword
 |      parameter displayof specifies a widget on the display
 |      to use. A keyword parameter type specifies the form of data to be
 |      fetched, defaulting to STRING except on X11, where UTF8_STRING is tried
 |      before STRING.
 |  
 |  selection_handle(self, command, **kw)
 |      Specify a function COMMAND to call if the X
 |      selection owned by this widget is queried by another
 |      application.
 |      
 |      This function must return the contents of the
 |      selection. The function will be called with the
 |      arguments OFFSET and LENGTH which allows the chunking
 |      of very long selections. The following keyword
 |      parameters can be provided:
 |      selection - name of the selection (default PRIMARY),
 |      type - type of the selection (e.g. STRING, FILE_NAME).
 |  
 |  selection_own(self, **kw)
 |      Become owner of X selection.
 |      
 |      A keyword parameter selection specifies the name of
 |      the selection (default PRIMARY).
 |  
 |  selection_own_get(self, **kw)
 |      Return owner of X selection.
 |      
 |      The following keyword parameter can
 |      be provided:
 |      selection - name of the selection (default PRIMARY),
 |      type - type of the selection (e.g. STRING, FILE_NAME).
 |  
 |  send(self, interp, cmd, *args)
 |      Send Tcl command CMD to different interpreter INTERP to be executed.
 |  
 |  setvar(self, name='PY_VAR', value='1')
 |      Set Tcl variable NAME to VALUE.
 |  
 |  size = grid_size(self)
 |      Return a tuple of the number of column and rows in the grid.
 |  
 |  slaves = pack_slaves(self)
 |      Return a list of all slaves of this widget
 |      in its packing order.
 |  
 |  tk_bisque(self)
 |      Change the color scheme to light brown as used in Tk 3.6 and before.
 |  
 |  tk_focusFollowsMouse(self)
 |      The widget under mouse will get automatically focus. Can not
 |      be disabled easily.
 |  
 |  tk_focusNext(self)
 |      Return the next widget in the focus order which follows
 |      widget which has currently the focus.
 |      
 |      The focus order first goes to the next child, then to
 |      the children of the child recursively and then to the
 |      next sibling which is higher in the stacking order.  A
 |      widget is omitted if it has the takefocus resource set
 |      to 0.
 |  
 |  tk_focusPrev(self)
 |      Return previous widget in the focus order. See tk_focusNext for details.
 |  
 |  tk_menuBar(self, *args)
 |      Do not use. Needed in Tk 3.6 and earlier.
 |  
 |  tk_setPalette(self, *args, **kw)
 |      Set a new color scheme for all widget elements.
 |      
 |      A single color as argument will cause that all colors of Tk
 |      widget elements are derived from this.
 |      Alternatively several keyword parameters and its associated
 |      colors can be given. The following keywords are valid:
 |      activeBackground, foreground, selectColor,
 |      activeForeground, highlightBackground, selectBackground,
 |      background, highlightColor, selectForeground,
 |      disabledForeground, insertBackground, troughColor.
 |  
 |  tk_strictMotif(self, boolean=None)
 |      Set Tcl internal variable, whether the look and feel
 |      should adhere to Motif.
 |      
 |      A parameter of 1 means adhere to Motif (e.g. no color
 |      change if mouse passes over slider).
 |      Returns the set value.
 |  
 |  unbind(self, sequence, funcid=None)
 |      Unbind for this widget for event SEQUENCE  the
 |      function identified with FUNCID.
 |  
 |  unbind_all(self, sequence)
 |      Unbind for all widgets for event SEQUENCE all functions.
 |  
 |  unbind_class(self, className, sequence)
 |      Unbind for a all widgets with bindtag CLASSNAME for event SEQUENCE
 |      all functions.
 |  
 |  update(self)
 |      Enter event loop until all pending events have been processed by Tcl.
 |  
 |  update_idletasks(self)
 |      Enter event loop until all idle callbacks have been called. This
 |      will update the display of windows but not process events caused by
 |      the user.
 |  
 |  wait_variable(self, name='PY_VAR')
 |      Wait until the variable is modified.
 |      
 |      A parameter of type IntVar, StringVar, DoubleVar or
 |      BooleanVar must be given.
 |  
 |  wait_visibility(self, window=None)
 |      Wait until the visibility of a WIDGET changes
 |      (e.g. it appears).
 |      
 |      If no parameter is given self is used.
 |  
 |  wait_window(self, window=None)
 |      Wait until a WIDGET is destroyed.
 |      
 |      If no parameter is given self is used.
 |  
 |  waitvar = wait_variable(self, name='PY_VAR')
 |      Wait until the variable is modified.
 |      
 |      A parameter of type IntVar, StringVar, DoubleVar or
 |      BooleanVar must be given.
 |  
 |  winfo_atom(self, name, displayof=0)
 |      Return integer which represents atom NAME.
 |  
 |  winfo_atomname(self, id, displayof=0)
 |      Return name of atom with identifier ID.
 |  
 |  winfo_cells(self)
 |      Return number of cells in the colormap for this widget.
 |  
 |  winfo_children(self)
 |      Return a list of all widgets which are children of this widget.
 |  
 |  winfo_class(self)
 |      Return window class name of this widget.
 |  
 |  winfo_colormapfull(self)
 |      Return true if at the last color request the colormap was full.
 |  
 |  winfo_containing(self, rootX, rootY, displayof=0)
 |      Return the widget which is at the root coordinates ROOTX, ROOTY.
 |  
 |  winfo_depth(self)
 |      Return the number of bits per pixel.
 |  
 |  winfo_exists(self)
 |      Return true if this widget exists.
 |  
 |  winfo_fpixels(self, number)
 |      Return the number of pixels for the given distance NUMBER
 |      (e.g. "3c") as float.
 |  
 |  winfo_geometry(self)
 |      Return geometry string for this widget in the form "widthxheight+X+Y".
 |  
 |  winfo_height(self)
 |      Return height of this widget.
 |  
 |  winfo_id(self)
 |      Return identifier ID for this widget.
 |  
 |  winfo_interps(self, displayof=0)
 |      Return the name of all Tcl interpreters for this display.
 |  
 |  winfo_ismapped(self)
 |      Return true if this widget is mapped.
 |  
 |  winfo_manager(self)
 |      Return the window mananger name for this widget.
 |  
 |  winfo_name(self)
 |      Return the name of this widget.
 |  
 |  winfo_parent(self)
 |      Return the name of the parent of this widget.
 |  
 |  winfo_pathname(self, id, displayof=0)
 |      Return the pathname of the widget given by ID.
 |  
 |  winfo_pixels(self, number)
 |      Rounded integer value of winfo_fpixels.
 |  
 |  winfo_pointerx(self)
 |      Return the x coordinate of the pointer on the root window.
 |  
 |  winfo_pointerxy(self)
 |      Return a tuple of x and y coordinates of the pointer on the root window.
 |  
 |  winfo_pointery(self)
 |      Return the y coordinate of the pointer on the root window.
 |  
 |  winfo_reqheight(self)
 |      Return requested height of this widget.
 |  
 |  winfo_reqwidth(self)
 |      Return requested width of this widget.
 |  
 |  winfo_rgb(self, color)
 |      Return tuple of decimal values for red, green, blue for
 |      COLOR in this widget.
 |  
 |  winfo_rootx(self)
 |      Return x coordinate of upper left corner of this widget on the
 |      root window.
 |  
 |  winfo_rooty(self)
 |      Return y coordinate of upper left corner of this widget on the
 |      root window.
 |  
 |  winfo_screen(self)
 |      Return the screen name of this widget.
 |  
 |  winfo_screencells(self)
 |      Return the number of the cells in the colormap of the screen
 |      of this widget.
 |  
 |  winfo_screendepth(self)
 |      Return the number of bits per pixel of the root window of the
 |      screen of this widget.
 |  
 |  winfo_screenheight(self)
 |      Return the number of pixels of the height of the screen of this widget
 |      in pixel.
 |  
 |  winfo_screenmmheight(self)
 |      Return the number of pixels of the height of the screen of
 |      this widget in mm.
 |  
 |  winfo_screenmmwidth(self)
 |      Return the number of pixels of the width of the screen of
 |      this widget in mm.
 |  
 |  winfo_screenvisual(self)
 |      Return one of the strings directcolor, grayscale, pseudocolor,
 |      staticcolor, staticgray, or truecolor for the default
 |      colormodel of this screen.
 |  
 |  winfo_screenwidth(self)
 |      Return the number of pixels of the width of the screen of
 |      this widget in pixel.
 |  
 |  winfo_server(self)
 |      Return information of the X-Server of the screen of this widget in
 |      the form "XmajorRminor vendor vendorVersion".
 |  
 |  winfo_toplevel(self)
 |      Return the toplevel widget of this widget.
 |  
 |  winfo_viewable(self)
 |      Return true if the widget and all its higher ancestors are mapped.
 |  
 |  winfo_visual(self)
 |      Return one of the strings directcolor, grayscale, pseudocolor,
 |      staticcolor, staticgray, or truecolor for the
 |      colormodel of this widget.
 |  
 |  winfo_visualid(self)
 |      Return the X identifier for the visual for this widget.
 |  
 |  winfo_visualsavailable(self, includeids=0)
 |      Return a list of all visuals available for the screen
 |      of this widget.
 |      
 |      Each item in the list consists of a visual name (see winfo_visual), a
 |      depth and if INCLUDEIDS=1 is given also the X identifier.
 |  
 |  winfo_vrootheight(self)
 |      Return the height of the virtual root window associated with this
 |      widget in pixels. If there is no virtual root window return the
 |      height of the screen.
 |  
 |  winfo_vrootwidth(self)
 |      Return the width of the virtual root window associated with this
 |      widget in pixel. If there is no virtual root window return the
 |      width of the screen.
 |  
 |  winfo_vrootx(self)
 |      Return the x offset of the virtual root relative to the root
 |      window of the screen of this widget.
 |  
 |  winfo_vrooty(self)
 |      Return the y offset of the virtual root relative to the root
 |      window of the screen of this widget.
 |  
 |  winfo_width(self)
 |      Return the width of this widget.
 |  
 |  winfo_x(self)
 |      Return the x coordinate of the upper left corner of this widget
 |      in the parent.
 |  
 |  winfo_y(self)
 |      Return the y coordinate of the upper left corner of this widget
 |      in the parent.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Misc:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Misc:
 |  
 |  getdouble = <class 'float'>
 |      float(x) -> floating point number
 |      
 |      Convert a string or number to a floating point number, if possible.
 |  
 |  getint = <class 'int'>
 |      int(x=0) -> integer
 |      int(x, base=10) -> integer
 |      
 |      Convert a number or string to an integer, or return 0 if no arguments
 |      are given.  If x is a number, return x.__int__().  For floating point
 |      numbers, this truncates towards zero.
 |      
 |      If x is not a number or if base is given, then x must be a string,
 |      bytes, or bytearray instance representing an integer literal in the
 |      given base.  The literal can be preceded by '+' or '-' and be surrounded
 |      by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |      Base 0 means to interpret the base from the string as an integer literal.
 |      >>> int('0b100', base=0)
 |      4
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Pack:
 |  
 |  forget = pack_forget(self)
 |      Unmap this widget and do not use it for the packing order.
 |  
 |  info = pack_info(self)
 |      Return information about the packing options
 |      for this widget.
 |  
 |  pack = pack_configure(self, cnf={}, **kw)
 |      Pack a widget in the parent widget. Use as options:
 |      after=widget - pack it after you have packed widget
 |      anchor=NSEW (or subset) - position widget according to
 |                                given direction
 |      before=widget - pack it before you will pack widget
 |      expand=bool - expand widget if parent size grows
 |      fill=NONE or X or Y or BOTH - fill widget if widget grows
 |      in=master - use master to contain this widget
 |      in_=master - see 'in' option description
 |      ipadx=amount - add internal padding in x direction
 |      ipady=amount - add internal padding in y direction
 |      padx=amount - add padding in x direction
 |      pady=amount - add padding in y direction
 |      side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.
 |  
 |  pack_configure(self, cnf={}, **kw)
 |      Pack a widget in the parent widget. Use as options:
 |      after=widget - pack it after you have packed widget
 |      anchor=NSEW (or subset) - position widget according to
 |                                given direction
 |      before=widget - pack it before you will pack widget
 |      expand=bool - expand widget if parent size grows
 |      fill=NONE or X or Y or BOTH - fill widget if widget grows
 |      in=master - use master to contain this widget
 |      in_=master - see 'in' option description
 |      ipadx=amount - add internal padding in x direction
 |      ipady=amount - add internal padding in y direction
 |      padx=amount - add padding in x direction
 |      pady=amount - add padding in y direction
 |      side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.
 |  
 |  pack_forget(self)
 |      Unmap this widget and do not use it for the packing order.
 |  
 |  pack_info(self)
 |      Return information about the packing options
 |      for this widget.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Place:
 |  
 |  place = place_configure(self, cnf={}, **kw)
 |      Place a widget in the parent widget. Use as options:
 |      in=master - master relative to which the widget is placed
 |      in_=master - see 'in' option description
 |      x=amount - locate anchor of this widget at position x of master
 |      y=amount - locate anchor of this widget at position y of master
 |      relx=amount - locate anchor of this widget between 0.0 and 1.0
 |                    relative to width of master (1.0 is right edge)
 |      rely=amount - locate anchor of this widget between 0.0 and 1.0
 |                    relative to height of master (1.0 is bottom edge)
 |      anchor=NSEW (or subset) - position anchor according to given direction
 |      width=amount - width of this widget in pixel
 |      height=amount - height of this widget in pixel
 |      relwidth=amount - width of this widget between 0.0 and 1.0
 |                        relative to width of master (1.0 is the same width
 |                        as the master)
 |      relheight=amount - height of this widget between 0.0 and 1.0
 |                         relative to height of master (1.0 is the same
 |                         height as the master)
 |      bordermode="inside" or "outside" - whether to take border width of
 |                                         master widget into account
 |  
 |  place_configure(self, cnf={}, **kw)
 |      Place a widget in the parent widget. Use as options:
 |      in=master - master relative to which the widget is placed
 |      in_=master - see 'in' option description
 |      x=amount - locate anchor of this widget at position x of master
 |      y=amount - locate anchor of this widget at position y of master
 |      relx=amount - locate anchor of this widget between 0.0 and 1.0
 |                    relative to width of master (1.0 is right edge)
 |      rely=amount - locate anchor of this widget between 0.0 and 1.0
 |                    relative to height of master (1.0 is bottom edge)
 |      anchor=NSEW (or subset) - position anchor according to given direction
 |      width=amount - width of this widget in pixel
 |      height=amount - height of this widget in pixel
 |      relwidth=amount - width of this widget between 0.0 and 1.0
 |                        relative to width of master (1.0 is the same width
 |                        as the master)
 |      relheight=amount - height of this widget between 0.0 and 1.0
 |                         relative to height of master (1.0 is the same
 |                         height as the master)
 |      bordermode="inside" or "outside" - whether to take border width of
 |                                         master widget into account
 |  
 |  place_forget(self)
 |      Unmap this widget.
 |  
 |  place_info(self)
 |      Return information about the placing options
 |      for this widget.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Grid:
 |  
 |  grid = grid_configure(self, cnf={}, **kw)
 |      Position a widget in the parent widget in a grid. Use as options:
 |      column=number - use cell identified with given column (starting with 0)
 |      columnspan=number - this widget will span several columns
 |      in=master - use master to contain this widget
 |      in_=master - see 'in' option description
 |      ipadx=amount - add internal padding in x direction
 |      ipady=amount - add internal padding in y direction
 |      padx=amount - add padding in x direction
 |      pady=amount - add padding in y direction
 |      row=number - use cell identified with given row (starting with 0)
 |      rowspan=number - this widget will span several rows
 |      sticky=NSEW - if cell is larger on which sides will this
 |                    widget stick to the cell boundary
 |  
 |  grid_configure(self, cnf={}, **kw)
 |      Position a widget in the parent widget in a grid. Use as options:
 |      column=number - use cell identified with given column (starting with 0)
 |      columnspan=number - this widget will span several columns
 |      in=master - use master to contain this widget
 |      in_=master - see 'in' option description
 |      ipadx=amount - add internal padding in x direction
 |      ipady=amount - add internal padding in y direction
 |      padx=amount - add padding in x direction
 |      pady=amount - add padding in y direction
 |      row=number - use cell identified with given row (starting with 0)
 |      rowspan=number - this widget will span several rows
 |      sticky=NSEW - if cell is larger on which sides will this
 |                    widget stick to the cell boundary
 |  
 |  grid_forget(self)
 |      Unmap this widget.
 |  
 |  grid_info(self)
 |      Return information about the options
 |      for positioning this widget in a grid.
 |  
 |  grid_remove(self)
 |      Unmap this widget but remember the grid options.
 |  
 |  location = grid_location(self, x, y)
 |      Return a tuple of column and row which identify the cell
 |      at which the pixel at position X and Y inside the master
 |      widget is located.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from XView:
 |  
 |  xview(self, *args)
 |      Query and change the horizontal position of the view.
 |  
 |  xview_moveto(self, fraction)
 |      Adjusts the view in the window so that FRACTION of the
 |      total width of the canvas is off-screen to the left.
 |  
 |  xview_scroll(self, number, what)
 |      Shift the x-view according to NUMBER which is measured in "units"
 |      or "pages" (WHAT).
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from YView:
 |  
 |  yview(self, *args)
 |      Query and change the vertical position of the view.
 |  
 |  yview_moveto(self, fraction)
 |      Adjusts the view in the window so that FRACTION of the
 |      total height of the canvas is off-screen to the top.
 |  
 |  yview_scroll(self, number, what)
 |      Shift the y-view according to NUMBER which is measured in
 |      "units" or "pages" (WHAT).

help> rectangle
no Python documentation found for 'rectangle'

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> list_icons = []
>>> for item in list_of_icon_coords:
	list_icons.append(canv.create_rectangle(x=item[0], y=item[1], height=item[3]-item[1]+1, width=item[2]-item[0]+1))

	
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    for item in list_of_icon_coords:
NameError: name 'list_of_icon_coords' is not defined
>>> import PeriodicCoordinateMap()
SyntaxError: invalid syntax
>>> import PeriodicCoordinateMap
>>> icon_map = PeriodicCoordinateMap()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    icon_map = PeriodicCoordinateMap()
TypeError: 'module' object is not callable
>>> from PeriodicCoordinateMap import *
>>> icon_map = PeriodicCoordinateMap()
>>> list_of_icon_coords = icon_map.getIconCoords()
>>> for item in list_of_icon_coords:
	list_icons.append(canv.create_rectangle(x=item[0], y=item[1], height=item[3]-item[1]+1, width=item[2]-item[0]+1))

	
Traceback (most recent call last):
  File "<pyshell#83>", line 2, in <module>
    list_icons.append(canv.create_rectangle(x=item[0], y=item[1], height=item[3]-item[1]+1, width=item[2]-item[0]+1))
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2331, in create_rectangle
    return self._create('rectangle', args, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2303, in _create
    cnf = args[-1]
IndexError: tuple index out of range
>>> for item in list_of_icon_coords:
	list_icons.append(canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1 )





			  )

	
>>> canv.find_all()
(5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128)
>>> for item in canv.find_all():
	if item > 5:
		canv.delete(item)

		
>>> canv.delete(5)
>>> image = canv.create_image((790/2,450/2), image=periodic_t)
>>> canv.find_all()
(129,)
>>> canv.bind("<Motion>", lambda event: on_motion(event, list_of_icon_coords))
'50159288<lambda>'
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
NameError: global name 'on_motion' is not defined

>>> 
>>> 
>>> 
>>> lbl = tkinter.Label()
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    lbl = tkinter.Label()
NameError: name 'tkinter' is not defined
>>> lbl = Label()
>>> lbl.pack(side=right)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    lbl.pack(side=right)
NameError: name 'right' is not defined
>>> lbl.pack_info()
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    lbl.pack_info()
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1919, in pack_info
    self.tk.call('pack', 'info', self._w))
_tkinter.TclError: window ".54385552" isn't packed
>>> lbl.pack_info
<bound method Label.pack_info of <tkinter.Label object at 0x033DDB90>>
>>> lbl.pack_info()
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    lbl.pack_info()
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1919, in pack_info
    self.tk.call('pack', 'info', self._w))
_tkinter.TclError: window ".54385552" isn't packed
>>> lbl.pack(side='right')
>>> lbl.configure(root=root, height=50, width=10)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    lbl.configure(root=root, height=50, width=10)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1263, in configure
    return self._configure('configure', cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-root"
>>> lbl.configure(root, height=50, width=10)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    lbl.configure(root, height=50, width=10)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1263, in configure
    return self._configure('configure', cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-menu"
>>> lbl = Label(root, height=50, width=50)
>>> lbl.pack(side='right')
>>> lbl.keys()
['activebackground', 'activeforeground', 'anchor', 'background', 'bd', 'bg', 'bitmap', 'borderwidth', 'compound', 'cursor', 'disabledforeground', 'fg', 'font', 'foreground', 'height', 'highlightbackground', 'highlightcolor', 'highlightthickness', 'image', 'justify', 'padx', 'pady', 'relief', 'state', 'takefocus', 'text', 'textvariable', 'underline', 'width', 'wraplength']
>>> def on_motion(event, coords_list):
	lbl.configure(text=coords_list)

	
>>> def on_motion(event, coords_list):
	lbl.configure(text=x, y)
	
SyntaxError: non-keyword arg after keyword arg
>>> def on_motion(event, coords_list):
	lbl.configure(text=)
	
SyntaxError: invalid syntax
>>> def on_motion(event, coords_list):
	loc = (event.x, event.y)
	lbl.configure(text=loc)

	
>>> 
>>> for item in list_of_icon_coords:
	list_icons.append(canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1 ))

	
>>> canv.find_all()
(129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249)
>>> for x in canv.find_all():
	if x > 129:
		canv.delete(x)

		
>>> for item in list_of_icon_coords:
	canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='blue')

	
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
>>> lbl.pack(side='bottom')
>>> lbl.pack(side='S')
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    lbl.pack(side='S')
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1909, in pack_configure
    + self._options(cnf, kw))
_tkinter.TclError: bad side "S": must be top, bottom, left, or right
>>> lbl.pack(side='bottom')
>>> lbl.pack_info()
{'side': 'bottom', 'fill': 'none', 'expand': '0', 'anchor': 'center', 'ipady': '0', 'ipadx': '0', 'in': <tkinter.Tk object at 0x0331AD70>, 'pady': '0', 'padx': '0'}
>>> lbl.pack(side='bottom', anchor='W')
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    lbl.pack(side='bottom', anchor='W')
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1909, in pack_configure
    + self._options(cnf, kw))
_tkinter.TclError: bad anchor "W": must be n, ne, e, se, s, sw, w, nw, or center
>>> lbl.pack(side='bottom', anchor='sw'

	 )
>>> lbl.pack(side='bottom', anchor='s')
>>> lbl.keys()
['activebackground', 'activeforeground', 'anchor', 'background', 'bd', 'bg', 'bitmap', 'borderwidth', 'compound', 'cursor', 'disabledforeground', 'fg', 'font', 'foreground', 'height', 'highlightbackground', 'highlightcolor', 'highlightthickness', 'image', 'justify', 'padx', 'pady', 'relief', 'state', 'takefocus', 'text', 'textvariable', 'underline', 'width', 'wraplength']
>>> lbl.configure(height=15, anchor='s')
>>> lbl.configure(height=15, anchor='sw'
	      )
>>> lbl.pack(side='left')
>>> lbl.tkraise()
>>> lbl.tkraise()
>>> lbl.tkraise()
>>> lbl.anchor
<bound method Label.grid_anchor of <tkinter.Label object at 0x033DDC10>>
>>> lbl.anchor('left)
	   
SyntaxError: EOL while scanning string literal
>>> lbl.anchor('left')
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    lbl.anchor('left')
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1314, in grid_anchor
    self.tk.call('grid', 'anchor', self._w, anchor)
_tkinter.TclError: bad anchor "left": must be n, ne, e, se, s, sw, w, nw, or center
>>> lbl.anchor('nw')
>>> lbl.lift
<bound method Label.tkraise of <tkinter.Label object at 0x033DDC10>>
>>> lbl.lift()
>>> lbl.lift9)
SyntaxError: invalid syntax
>>> lbl.lift()
>>> lbl.location
<bound method Label.grid_location of <tkinter.Label object at 0x033DDC10>>
>>> lbl.location()
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    lbl.location()
TypeError: grid_location() missing 2 required positional arguments: 'x' and 'y'
>>> lbl.location(0, 0)
(0, 0)
>>> lblfr_periodic.pack(side='right')
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    lblfr_periodic.pack(side='right')
NameError: name 'lblfr_periodic' is not defined
>>> lblfr.periodic.pack(side='right')
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    lblfr.periodic.pack(side='right')
AttributeError: 'Labelframe' object has no attribute 'periodic'
>>> lblfr.pack(side='right')
>>> lbl.pack(side='top')
>>> lbl.anchor('nw')
>>> lblfr.configure(height = 250)
>>> lblfr.configure(expand=0)
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    lblfr.configure(expand=0)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1263, in configure
    return self._configure('configure', cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-expand"
>>> lblfr.keys()
['labelanchor', 'text', 'underline', 'labelwidget', 'borderwidth', 'padding', 'relief', 'width', 'height', 'takefocus', 'cursor', 'style', 'class']
>>> lblfr.pack_info()
{'side': 'right', 'fill': 'both', 'expand': '1', 'anchor': 'w', 'ipady': '0', 'ipadx': '0', 'in': <tkinter.Tk object at 0x0331AD70>, 'pady': '10', 'padx': '10'}
>>> lblfr.pack(expand=0)
>>> lblfr.pack_info()
{'side': 'right', 'fill': 'both', 'expand': '0', 'anchor': 'w', 'ipady': '0', 'ipadx': '0', 'in': <tkinter.Tk object at 0x0331AD70>, 'pady': '10', 'padx': '10'}
>>> lblfr.pack(side='top' fill='none')
SyntaxError: invalid syntax
>>> lblfr.pack(side='top' fill='0')
SyntaxError: invalid syntax
>>> lblfr.pack(side='top' fill='None')
SyntaxError: invalid syntax
>>> lblfr.pack(side='top')
>>> def on_motion(event, coords_list):
	loc = (event.x, event.y)
	lbl.configure(text=loc)
	for item in coords_list):
		
SyntaxError: invalid syntax
>>> def on_motion(event, coords_list):
	loc = (event.x, event.y)
	lbl.configure(text=loc)
	for item in coords_list:
		if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			highlight=canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')
		else:
			canv.delete(highlight)
			highlight=0

			
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
highlight = 0
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#188>", line 8, in on_motion
UnboundLocalError: local variable 'highlight' referenced before assignment
def on_motion(event, coords_list):
	loc = (event.x, event.y)
	lbl.configure(text=loc)
	highlight=0
	for item in coords_list:
		if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			highlight=canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')
		else:
			canv.delete(highlight)
			highlight=0

>>> def on_motion(event, coords_list):
	loc = (event.x, event.y)
	lbl.configure(text=loc)
	highlight=0
	for item in coords_list:
		if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			highlight=canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')
			highlight.pack()
		else:
			canv.delete(highlight)
			highlight=0

>>> 
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#191>", line 8, in on_motion
AttributeError: 'int' object has no attribute 'pack'
def on_motion(event, coords_list):
	loc = (event.x, event.y)
	lbl.configure(text=loc)
	highlight=0
	for item in coords_list:
		if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			highlight=canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')
		else:
			canv.delete(highlight)
			highlight=0

			
>>> canv.find_all()
(129, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539)
>>> canv.delete(item) if item > 369 for item in cavn.find_all()
SyntaxError: invalid syntax
>>> [canv.delete(item) if item > 369 for item in cavn.find_all()]
SyntaxError: invalid syntax
>>> if item > 369 canv.delete(item) for item in cavn.find_all()
SyntaxError: invalid syntax
>>> canv.delete(item) for item in cavn.find_all() if item > 369
SyntaxError: invalid syntax
>>> for item in cavn.find_all() if item > 369 canv.delete(item)
SyntaxError: invalid syntax
>>> for item in cavn.find_all() if (item > 369) canv.delete(item)
SyntaxError: invalid syntax
>>> canv.delete(item) if (item > 369) for item in cavn.find_all()
SyntaxError: invalid syntax
>>> canv.delete(item) if (item > 369)
SyntaxError: invalid syntax
>>> canv.delete(item) if (item > 369) for item in canv.find_all()
SyntaxError: invalid syntax
>>> [canv.delete(item) if (item > 369) for item in canv.find_all()]
SyntaxError: invalid syntax
>>> [canv.delete(item) if (item > 369)] for item in canv.find_all()
SyntaxError: invalid syntax
>>> for item in canv.find_all():
	canv.delete(item) if (item > 369)
	
SyntaxError: invalid syntax
>>> for item in canv.find_all():
	if (item > 369):
		canv.delete(item)

		
>>> canv.find_all()
(129, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369)
>>> def on_motion(event, coords_list):
	loc = (event.x, event.y)
	lbl.configure(text=loc)
	for item in coords_list:
		if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')
		else:
			canv.delete(len(canv.find_all()-1))

			
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#216>", line 8, in on_motion
TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
def on_motion(event, coords_list):
	loc = (event.x, event.y)
	lbl.configure(text=loc)
	for item in coords_list:
		if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> 
>>> canv.find_all()
(129, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840)
>>> len(canv.find_all())
145
>>> canv.create_rectangle.keys()
Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    canv.create_rectangle.keys()
AttributeError: 'function' object has no attribute 'keys'
>>> canv.create_rectangle.__getattribute__
<method-wrapper '__getattribute__' of method object at 0x03029B20>
>>> canv.create_rectangle.__getattribute__()
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    canv.create_rectangle.__getattribute__()
TypeError: expected 1 arguments, got 0
>>> canv.create_rectangle.__getattribute__(self)
Traceback (most recent call last):
  File "<pyshell#224>", line 1, in <module>
    canv.create_rectangle.__getattribute__(self)
NameError: name 'self' is not defined
>>> canv.keys()
['background', 'bd', 'bg', 'borderwidth', 'closeenough', 'confine', 'cursor', 'height', 'highlightbackground', 'highlightcolor', 'highlightthickness', 'insertbackground', 'insertborderwidth', 'insertofftime', 'insertontime', 'insertwidth', 'offset', 'relief', 'scrollregion', 'selectbackground', 'selectborderwidth', 'selectforeground', 'state', 'takefocus', 'width', 'xscrollcommand', 'xscrollincrement', 'yscrollcommand', 'yscrollincrement']
>>> help(Canvas.create_rectangle)
Help on function create_rectangle in module tkinter:

create_rectangle(self, *args, **kw)
    Create rectangle with coordinates x1,y1,x2,y2.

>>> canv.focus_lastfor
<bound method Canvas.focus_lastfor of <tkinter.Canvas object at 0x0331A490>>
>>> canv.focus_lastfor()
<tkinter.Tk object at 0x0331AD70>
>>> canv.index()
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    canv.index()
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2392, in index
    return getint(self.tk.call((self._w, 'index') + args))
_tkinter.TclError: wrong # args: should be ".53584656.53585040 index tagOrId string"
>>> canv.index(1)
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    canv.index(1)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2392, in index
    return getint(self.tk.call((self._w, 'index') + args))
_tkinter.TclError: wrong # args: should be ".53584656.53585040 index tagOrId string"
>>> canv.index(369)
Traceback (most recent call last):
  File "<pyshell#231>", line 1, in <module>
    canv.index(369)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2392, in index
    return getint(self.tk.call((self._w, 'index') + args))
_tkinter.TclError: wrong # args: should be ".53584656.53585040 index tagOrId string"
>>> canv.find_all()
(129, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840)
>>> canv.find(0)
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    canv.find(0)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2352, in find
    self.tk.call((self._w, 'find') + args)) or ()
_tkinter.TclError: bad search command "0": must be above, all, below, closest, enclosed, overlapping, or withtag
>>> canv.find(129)
Traceback (most recent call last):
  File "<pyshell#234>", line 1, in <module>
    canv.find(129)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2352, in find
    self.tk.call((self._w, 'find') + args)) or ()
_tkinter.TclError: bad search command "129": must be above, all, below, closest, enclosed, overlapping, or withtag
>>> canv.find(all)
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    canv.find(all)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2352, in find
    self.tk.call((self._w, 'find') + args)) or ()
_tkinter.TclError: bad search command "<built-in function all>": must be above, all, below, closest, enclosed, overlapping, or withtag
>>> canv.coords
<bound method Canvas.coords of <tkinter.Canvas object at 0x0331A490>>
>>> canv.coords()
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    canv.coords()
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2299, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: wrong # args: should be ".53584656.53585040 coords tagOrId ?x y x y ...?"
>>> def on_motion(event, coords_list):
	loc = (event.x, event.y, canv.find_withtag('CURRENT')
	lbl.configure(text=loc)
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

SyntaxError: invalid syntax
>>> def on_motion(event, coords_list):
	loc = (event.x, event.y, canv.find_withtag('CURRENT'))
	lbl.configure(text=loc)
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

	
>>> def on_motion(event, coords_list):
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

	
>>> def create_map_items(self):
	for item in list_of_icon_coords:
		canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, fill='', outline='blue', activeoutline='green')

		
>>> def create_map_items(self):
	for item in list_of_icon_coords:
		canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, fill='', outline='blue', activeoutline='green', tags='icon' )

		
>>> def create_icons(self):
	for item in list_of_icon_coords:
		canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, fill='', outline='blue', activeoutline='green', tags='icon' )

		
>>> def delete_icons(self):
	for item in canv.find_withtag('icon'):
		delete(item)

		
>>> canv.find_all()
(129, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840)
>>> for item in canv.find_all()
SyntaxError: invalid syntax
>>> for item in canv.find_all():
	if item >=250:
		delete(item)

		
Traceback (most recent call last):
  File "<pyshell#260>", line 3, in <module>
    delete(item)
NameError: name 'delete' is not defined
>>> for item in canv.find_all():
	if item >=250:
		canv.delete(item)

		
>>> canv.find_all()
(129,)
>>> def delete_icons(self, canvas_item):
	for item in canvas_item.find_withtag('icon'):
		canvas_item.delete(item)

		
>>> def create_icons(self, canvas_item, list_of_icon_coords):
	for item in list_of_icon_coords:
		canvas_item.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, fill='', outline='blue', activeoutline='green', tags='icon' )

		
>>> def create_icons(self, canvas_item, list_of_icon_coords):
	for item in list_of_icon_coords:
		canvas_item.create_rectangle(item[0], item[1], item[2]+2, item[3]+2, fill='', outline='blue', activeoutline='green', tags='icon' )

		
>>> create_icons(canv, list_of_icon_coords)
Traceback (most recent call last):
  File "<pyshell#270>", line 1, in <module>
    create_icons(canv, list_of_icon_coords)
TypeError: create_icons() missing 1 required positional argument: 'list_of_icon_coords'
>>> create_icons(self, canv, list_of_icon_coords)
Traceback (most recent call last):
  File "<pyshell#271>", line 1, in <module>
    create_icons(self, canv, list_of_icon_coords)
NameError: name 'self' is not defined
>>> create_icons(canv, list_of_icon_coords)
Traceback (most recent call last):
  File "<pyshell#272>", line 1, in <module>
    create_icons(canv, list_of_icon_coords)
TypeError: create_icons() missing 1 required positional argument: 'list_of_icon_coords'
>>> def create_icons(canvas_item, list_of_icon_coords):
	for item in list_of_icon_coords:
		canvas_item.create_rectangle(item[0], item[1], item[2]+2, item[3]+2, fill='', outline='blue', activeoutline='green', tags='icon' )

		
>>> create_icons(canv, list_of_icon_coords)
>>> delete_icons()
Traceback (most recent call last):
  File "<pyshell#276>", line 1, in <module>
    delete_icons()
TypeError: delete_icons() missing 2 required positional arguments: 'self' and 'canvas_item'
>>> def delete_icons(canvas_item):
	for item in canvas_item.find_withtag('icon'):
		canvas_item.delete(item)

		
>>> delete_icons(canvas_item)
Traceback (most recent call last):
  File "<pyshell#279>", line 1, in <module>
    delete_icons(canvas_item)
NameError: name 'canvas_item' is not defined
>>> delete_icons(canv)
>>> def create_icons(canvas_item, list_of_icon_coords):
	for item in list_of_icon_coords:
		canvas_item.create_rectangle(item[0], item[1], item[2], item[3], fill='', outline='blue', activeoutline='green', tags='icon' )

		
>>> create_icons(canv, list_of_icon_coords)
>>> 
>>> 
>>> 
>>> def on_motion(event, coords_list):
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

	
>>> def on_motion(event, coords_list):
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	if 'icon' in canv.gettags(closest):
		closest.configure(state='ACTIVE')
	else:
		closest.configure(state='NORMAL')
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 6, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 6, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#290>", line 8, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
def on_motion(event, coords_list):
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	print(closest)
	if 'icon' in canv.gettags(closest):
		closest.configure(state='ACTIVE')
	else:
		closest.configure(state='NORMAL')
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> (1024,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1072,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(129,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 9, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(129,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 9, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1024,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1072,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(129,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 9, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1072,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1072,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1072,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1072,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1072,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1072,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1072,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(129,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 9, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(129,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 9, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1072,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1072,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1072,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1072,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1074,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1074,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1074,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1072,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1074,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1074,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1074,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1072,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
(1024,)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#292>", line 7, in on_motion
AttributeError: 'tuple' object has no attribute 'configure'
def on_motion(event, coords_list):
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	print(closest)
	print(canv.gettags(closest))
	
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

	
>>> (129,)
('current',)
(129,)
('current',)
(129,)
('current',)
(129,)
('current',)
(1070,)
('icon',)
(129,)
('current',)
(129,)
('current',)
(129,)
('current',)
(129,)
('current',)
(129,)
('current',)
(129,)
('current',)
(129,)
('current',)
(129,)
('current',)
(129,)
('current',)
(129,)
('current',)
(1070,)
('icon',)
(1070,)
('icon',)
(1070,)
('icon', 'current')
(1070,)
('icon', 'current')
(1070,)
('icon', 'current')
(1070,)
('icon', 'current')
(129,)
('current',)
(1018,)
('icon',)
(1018,)
('icon',)
(1018,)
('icon', 'current')
(1018,)
('icon', 'current')
(1018,)
('icon',)
(1018,)
('icon',)
(129,)
('current',)
(1070,)
('icon',)
(1069,)
('icon',)
(1069,)
('icon',)
(1069,)
('icon', 'current')
(1069,)
('icon', 'current')
(1069,)
('icon', 'current')
(1069,)
('icon', 'current')
(1069,)
('icon', 'current')
(1069,)
('icon', 'current')
(1069,)
('icon', 'current')
(1069,)
('icon',)
(1017,)
('icon', 'current')
(1017,)
('icon', 'current')
(1017,)
('icon', 'current')
(1017,)
('icon',)
(129,)
('current',)
(1017,)
('icon',)
(1017,)
('icon',)
(1017,)
('icon',)
(1017,)
('icon', 'current')
def on_motion(event, coords_list):
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	print(closest)
	if 'icon' in canv.gettags(closest)):
		print(canv.gettags(closest))
	
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')
		
SyntaxError: invalid syntax
>>> 
>>> def on_motion(event, coords_list):
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	print(closest)
	if 'icon' in canv.gettags(closest):
		print(canv.gettags(closest))
	
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> (1074,)
('icon',)
(1030,)
('icon', 'current')
(1030,)
('icon', 'current')
(1030,)
('icon', 'current')
(1030,)
('icon',)
(1024,)
('icon',)
(129,)
(129,)
(129,)
(129,)
(129,)
(129,)
(129,)
(1072,)
('icon',)
(1072,)
('icon', 'current')
(1072,)
('icon', 'current')
(1074,)
('icon',)
(1074,)
('icon',)
(1072,)
('icon',)
(1072,)
('icon',)
(1072,)
('icon',)
(129,)
(129,)
(129,)
(1024,)
('icon',)
(1024,)
('icon',)
(1024,)
('icon',)
(129,)
(129,)
(1072,)
('icon',)
(1072,)
('icon',)
(1072,)
('icon', 'current')
(1072,)
('icon',)
(1072,)
('icon',)
(1072,)
('icon',)
(1071,)
('icon',)
(1071,)
('icon',)
(1072,)
('icon',)
(1072,)
('icon',)
(1072,)
('icon',)
(1072,)
('icon',)
(1072,)
('icon', 'current')
(1072,)
('icon', 'current')
(1072,)
('icon',)
(1072,)
('icon',)
(1072,)
('icon',)
(129,)
(129,)
(129,)
(129,)
(1024,)
('icon',)
(1024,)
('icon', 'current')
(1024,)
('icon',)
(129,)
(129,)
(129,)
(1072,)
('icon',)
(1072,)
('icon', 'current')
(1072,)
('icon', 'current')
(1072,)
('icon', 'current')
(1072,)
('icon', 'current')
(1072,)
('icon', 'current')
(1072,)
('icon', 'current')
(1072,)
('icon', 'current')
(1072,)
('icon', 'current')
(1072,)
('icon', 'current')
(1072,)
('icon', 'current')
(1072,)
('icon', 'current')
(1072,)
('icon',)
(1072,)
('icon',)
(1072,)
('icon',)
(1024,)
('icon',)
(1024,)
('icon',)
(1018,)
('icon',)
(129,)
(129,)
(129,)
(129,)
(1018,)
('icon',)
(1018,)
('icon',)
(1018,)
('icon',)
(1018,)
('icon',)
(1018,)
('icon',)
(129,)
(129,)
(1018,)
('icon',)
(1018,)
('icon',)
(1024,)
('icon',)
(1018,)
('icon',)
(1018,)
('icon',)
(129,)
(129,)
(129,)
(129,)
(129,)
(129,)
(1018,)
('icon',)
(1018,)
('icon', 'current')
def on_motion(event, coords_list):
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	if 'icon' in canv.gettags(closest):
		print(closest, canv.gettags(closest))
		canv.itemconfig(state='Active')
				
	
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> (1052,) ('icon',)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#300>", line 7, in on_motion
TypeError: itemconfigure() missing 1 required positional argument: 'tagOrId'
(1052,) ('icon',)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#300>", line 7, in on_motion
TypeError: itemconfigure() missing 1 required positional argument: 'tagOrId'
(1052,) ('icon', 'current')
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#300>", line 7, in on_motion
TypeError: itemconfigure() missing 1 required positional argument: 'tagOrId'
def on_motion(event, coords_list):
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	if 'icon' in canv.gettags(closest):
		print(closest, canv.gettags(closest))
		canv.itemconfig(closest, state='Active')
				
	
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> (1018,) ('icon', 'current')
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#302>", line 7, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: bad state value "Active": must be normal, hidden, or disabled
(1018,) ('icon',)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#302>", line 7, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: bad state value "Active": must be normal, hidden, or disabled
(1026,) ('icon',)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#302>", line 7, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: bad state value "Active": must be normal, hidden, or disabled
def on_motion(event, coords_list):
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	if 'icon' in canv.gettags(closest):
		print(closest, canv.gettags(closest))
		canv.itemconfig(closest, state='ACTIVE')
				
	
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> (1018,) ('icon', 'current')
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#304>", line 7, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: bad state value "ACTIVE": must be normal, hidden, or disabled
(1018,) ('icon',)
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#304>", line 7, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: bad state value "ACTIVE": must be normal, hidden, or disabled
def on_motion(event, coords_list):
	
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	if 'icon' in canv.gettags(closest):
		print(closest, canv.gettags(closest))
		canv.itemconfig(closest, outline='green')
		
	
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> (1052,) ('icon',)
(1052,) ('icon',)
(1052,) ('icon',)
(1054,) ('icon', 'current')
(1054,) ('icon', 'current')
(1054,) ('icon',)
(1054,) ('icon', 'current')
(1054,) ('icon', 'current')
(1054,) ('icon',)
(1054,) ('icon',)
(1052,) ('icon',)
(1052,) ('icon',)
(1056,) ('icon',)
(1056,) ('icon', 'current')
(1056,) ('icon', 'current')
(1056,) ('icon',)
(1056,) ('icon',)
(1056,) ('icon',)
(1056,) ('icon',)
(1056,) ('icon',)
(1056,) ('icon',)
(1056,) ('icon',)
(1054,) ('icon', 'current')
(1054,) ('icon',)
(1054,) ('icon',)
(1052,) ('icon', 'current')
(1051,) ('icon',)
(1051,) ('icon', 'current')
(979,) ('icon',)
(1052,) ('icon', 'current')
(1054,) ('icon', 'current')
(1055,) ('icon', 'current')
(1055,) ('icon',)
(1053,) ('icon', 'current')
(1053,) ('icon',)
(970,) ('icon',)
(970,) ('icon',)
(970,) ('icon',)
(970,) ('icon',)
(970,) ('icon',)
(975,) ('icon', 'current')
(975,) ('icon',)
(971,) ('icon',)
(971,) ('icon',)
(971,) ('icon',)
(971,) ('icon',)
(970,) ('icon', 'current')
(966,) ('icon', 'current')
(965,) ('icon',)
(966,) ('icon', 'current')
(966,) ('icon',)
(967,) ('icon',)
(967,) ('icon',)
def on_motion(event, coords_list):
	
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	if 'icon' in canv.gettags(closest) and 'current' in canv.gettags(closest):
		print(closest, canv.gettags(closest))
		canv.itemconfig(closest, outline='green')
	elif 'icon' in canv.gettages(closest) and not 'current' in canv.gettags(closest):
		canv.itemconfig(closest, outline='blue')
		
	
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#308>", line 9, in on_motion
AttributeError: 'Canvas' object has no attribute 'gettages'
def on_motion(event, coords_list):
	
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	if 'icon' in canv.gettags(closest) and 'current' in canv.gettags(closest):
		print(closest, canv.gettags(closest))
		canv.itemconfig(closest, outline='green')
	elif 'icon' in canv.gettags(closest) and not 'current' in canv.gettags(closest):
		canv.itemconfig(closest, outline='blue')
		
	
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

>>> (1056,) ('icon', 'current')
(1056,) ('icon', 'current')
(1056,) ('icon', 'current')
(1056,) ('icon', 'current')
(1056,) ('icon', 'current')
(1056,) ('icon', 'current')
(1056,) ('icon', 'current')
(1056,) ('icon', 'current')
(1056,) ('icon', 'current')
(1056,) ('icon', 'current')
(1056,) ('icon', 'current')
(1058,) ('icon', 'current')
(1054,) ('icon', 'current')
(1054,) ('icon', 'current')
(1054,) ('icon', 'current')
(1054,) ('icon', 'current')
def on_motion(event, coords_list):
	
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	if 'icon' in canv.gettags(closest) and 'current' in canv.gettags(closest):
		print(closest, canv.gettags(closest))
		canv.itemconfig(closest, outline='green')
	else:
		canv.itemconfig(closest, outline='blue')
		
	
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
(1056,) ('icon', 'current')
(1056,) ('icon', 'current')
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
(1052,) ('icon', 'current')
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
(1054,) ('icon', 'current')
(1052,) ('icon', 'current')
(1052,) ('icon', 'current')
(1052,) ('icon', 'current')
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
(975,) ('icon', 'current')
(975,) ('icon', 'current')
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
(971,) ('icon', 'current')
(971,) ('icon', 'current')
(971,) ('icon', 'current')
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#310>", line 10, in on_motion
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2408, in itemconfigure
    return self._configure(('itemconfigure', tagOrId), cnf, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1254, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-outline"
def on_motion(event, coords_list):
	
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	try:
		if 'icon' in canv.gettags(closest) and 'current' in canv.gettags(closest):
			print(closest, canv.gettags(closest))
			canv.itemconfig(closest, outline='green')
		else:
			canv.itemconfig(closest, outline='blue')
	catch(Empty):
		print(closest, canv.gettags(closest))
		
	
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')
		
SyntaxError: invalid syntax
>>> def on_motion(event, coords_list):
	
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	try:
		if 'icon' in canv.gettags(closest) and 'current' in canv.gettags(closest):
			print(closest, canv.gettags(closest))
			canv.itemconfig(closest, outline='green')
		else:
			canv.itemconfig(closest, outline='blue')
	except TclError:
		print(closest, canv.gettags(closest))
		
	
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> (129,) ('current',)
(129,) ('current',)
(129,) ('current',)
(1054,) ('icon', 'current')
(129,) ('current',)
(129,) ('current',)
(129,) ('current',)
(129,) ('current',)
(129,) ('current',)
(129,) ('current',)
(129,) ('current',)
(129,) ('current',)
(129,) ('current',)
(129,) ('current',)
(129,) ('current',)
(129,) ('current',)
(129,) ('current',)
(129,) ('current',)
(1052,) ('icon', 'current')
(1052,) ('icon', 'current')
(129,) ('current',)
(129,) ('current',)
(129,) ('current',)
(129,) ('current',)
(129,) ()
def on_motion(event, coords_list):
	
	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	try:
		if 'icon' in canv.gettags(closest) and 'current' in canv.gettags(closest):
			print(closest, canv.gettags(closest))
			canv.itemconfig(closest, outline='green')
		else:
			canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))
		
	
	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(1054,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
def on_motion(event, coords_list):

	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	try:
		if 'icon' in canv.gettags(closest) and 'current' in canv.gettags(closest):
			print(closest, canv.gettags(closest))
			canv.itemconfig(closest, outline='green')
		else:
			canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> (1015,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(975,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(975,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(1054,) ('icon', 'current')
(1054,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(1054,) ('icon', 'current')
(1054,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
def on_motion(event, coords_list):

	current = canv.find_withtag('current')
	loc = (event.x, event.y, current)
	lbl.configure(text=loc)
	
	
	try:
		if 'icon' in current:
			print(current)
			canv.itemconfig(current, outline='green')
		#else:
		#	canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

>>> def on_motion(event, coords_list):

	loc = (event.x, event.y, canv.find_withtag('current'))
	lbl.configure(text=loc)
	closest = canv.find_closest(event.x, event.y, halo=5)
	try:
		if 'icon' in canv.gettags(closest) and 'current' in canv.gettags(closest):
			print(closest, canv.gettags(closest))
			canv.itemconfig(closest, outline='green')
		else:
			canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> ERROR:  (129,) ('current',)
(1068,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(1068,) ('icon', 'current')
ERROR:  (129,) ()
ERROR:  (129,) ()
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(1052,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(1052,) ('icon', 'current')
(1052,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(1052,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(1052,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(1052,) ('icon', 'current')
(1052,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(1052,) ('icon', 'current')
(1052,) ('icon', 'current')
(1052,) ('icon', 'current')
(1052,) ('icon', 'current')
(1052,) ('icon', 'current')
(1052,) ('icon', 'current')
(1052,) ('icon', 'current')
(1052,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(967,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(1052,) ('icon', 'current')
(1052,) ('icon', 'current')
(1052,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(1051,) ('icon', 'current')
(1051,) ('icon', 'current')
(1051,) ('icon', 'current')
(1051,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(971,) ('icon', 'current')
(971,) ('icon', 'current')
(971,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(965,) ('icon', 'current')
(965,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(966,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(970,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(971,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(971,) ('icon', 'current')
ERROR:  (129,) ('current',)
(1054,) ('icon', 'current')
(1054,) ('icon', 'current')
(1054,) ('icon', 'current')
(1054,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(1068,) ('icon', 'current')
(1068,) ('icon', 'current')
(1068,) ('icon', 'current')
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
(1068,) ('icon', 'current')
ERROR:  (129,) ('current',)
def on_motion(event, coords_list):

	current = canv.find_withtag('current')
	loc = (event.x, event.y, current)
	lbl.configure(text=loc)
	
	
	try:
		if 'icon' in current:
			print(current)
			canv.itemconfig(current, outline='green')
		#else:
		#	canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> def on_motion(event, coords_list):

	current = canv.find_withtag('current')
	loc = (event.x, event.y, current)
	lbl.configure(text=loc)


	try:
		if 'icon' in current:
			print(current)
			canv.itemconfig(current, outline='green')
		#else:
		#	canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> 
>>> def on_motion(event, coords_list):

	current = canv.find_withtag('current')
	closest = canv.find_closest(event.x, event.y, 1)
	loc = (event.x, event.y, current)
	lbl.configure(text=loc)


	try:
		if 'icon' in closest:
			print("Closest, Current:", closest, current)
			canv.itemconfig(current, outline='green')
		#else:
		#	canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> def on_motion(event, coords_list):

	current = canv.find_withtag('current')
	closest = canv.find_closest(event.x, event.y, 1)
	loc = (event.x, event.y, current)
	lbl.configure(text=loc)


	try:
		if 'icon' in closest:
			print("Closest, Current:", closest, current)
			canv.itemconfig(closest, outline='green')
		#else:
		#	canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> def on_motion(event, coords_list):

	current = canv.find_withtag('current')
	closest = canv.find_closest(event.x, event.y, 1)
	loc = (event.x, event.y, current)
	lbl.configure(text=loc)


	try:
		if 'icon' in closest:
			print("Closest, Current:", closest, current)
			selected = closest
			canv.itemconfig(selected, outline='green')
		#else:
		#	canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> def on_motion(event, coords_list):

	current = canv.find_withtag('current')
	closest = canv.find_closest(event.x, event.y, 1)
	loc = (event.x, event.y, current)
	lbl.configure(text=loc)


	try:
		if 'icon' in closest and 'icon' in current:
			print("Closest, Current:", closest, current)
			selected = closest
			canv.itemconfig(selected, outline='green')
		else:
			canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> 
>>> ERROR:  (129,) ()
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
ERROR:  (129,) ('current',)
def on_motion(event, coords_list):

	current = canv.find_withtag('current')
	closest = canv.find_closest(event.x, event.y, 1)
	loc = (event.x, event.y, current)
	lbl.configure(text=loc)


	try:
		if 'icon' in closest and 'icon' in current:
			print("Closest, Current:", closest, current)
			selected = closest
			canv.itemconfig(selected, outline='green')
		#else:
			#canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

>>> 
>>> p
Traceback (most recent call last):
  File "<pyshell#337>", line 1, in <module>
    p
NameError: name 'p' is not defined
>>> def on_motion(event, coords_list):

	current = canv.find_withtag('current')
	closest = canv.find_closest(event.x, event.y, 1)
	loc = (event.x, event.y, current)
	lbl.configure(text=loc)


	try:
		if 'icon' in current:
			print("Closest, Current:", closest, current)
			selected = closest
			canv.itemconfig(selected, outline='green')
		#else:
			#canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> def on_motion(event, coords_list):

	current = canv.find_withtag('current')
	closest = canv.find_closest(event.x, event.y, 1)
	loc = (event.x, event.y, current)
	lbl.configure(text=loc)


	try:
		if 'icon' in current:
			print("Closest, Current:", closest, current)
			selected = closest
			canv.itemconfig(selected, highlightcolor="green")
		#else:
			#canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> def on_motion(event, coords_list):

	current = canv.find_withtag('current')
	closest = canv.find_closest(event.x, event.y, 1)
	loc = (event.x, event.y, current)
	lbl.configure(text=loc)


	try:
		if 'icon' in current:
			print("Closest, Current:", closest, current)
			selected = closest
			canv.itemconfig(selected, highlightcolor="green")
			canv.focus(selected)
		#else:
			#canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> delete_icons(canv)
>>> create_icons(canv, list_of_icon_coords)
>>> print(create_icons)
<function create_icons at 0x03398DF8>
>>> print(create_icons())
Traceback (most recent call last):
  File "<pyshell#347>", line 1, in <module>
    print(create_icons())
TypeError: create_icons() missing 2 required positional arguments: 'canvas_item' and 'list_of_icon_coords'
>>> create_icons()
Traceback (most recent call last):
  File "<pyshell#348>", line 1, in <module>
    create_icons()
TypeError: create_icons() missing 2 required positional arguments: 'canvas_item' and 'list_of_icon_coords'
>>> help(create_icons)
Help on function create_icons in module __main__:

create_icons(canvas_item, list_of_icon_coords)

>>> def create_icons(canvas_item, list_of_icon_coords):
	for item in list_of_icon_coords:
		canvas_item.create_rectangle(item[0], item[1], item[2], item[3], fill='', outline='blue', activeoutline='green', tags='icon', highlightcolor='red' )

		
>>> delete_icons(canv)
>>> def create_icons(canvas_item, list_of_icon_coords):
	for item in list_of_icon_coords:
		canvas_item.create_rectangle(item[0], item[1], item[2], item[3], fill='', outline='blue', tags='icon', highlightcolor='red' )

		
>>> def on_motion(event, coords_list):

	current = canv.find_withtag('current')
	closest = canv.find_closest(event.x, event.y, 1)
	loc = (event.x, event.y, current)
	lbl.configure(text=loc)


	try:
		if 'icon' in current:
			print("Closest, Current:", closest, current)
			selected = closest
			canv.focus(selected)
		#else:
			#canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

>>> 
>>> def on_motion(event, coords_list):
	set_focus(canv)
	current = canv.find_withtag('current')
	closest = canv.find_closest(event.x, event.y, 1)
	loc = (event.x, event.y, current)
	lbl.configure(text=loc)


	try:
		if 'icon' in current:
			print("Closest, Current:", closest, current)
			selected = closest
			canv.focus(selected)
		#else:
			#canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
During handling of the above exception, another exception occurred:
	
SyntaxError: invalid syntax
>>> 
>>> Canvas.set_focus(canv)
Traceback (most recent call last):
  File "<pyshell#361>", line 1, in <module>
    Canvas.set_focus(canv)
AttributeError: type object 'Canvas' has no attribute 'set_focus'
>>> canv.set_focus()
Traceback (most recent call last):
  File "<pyshell#362>", line 1, in <module>
    canv.set_focus()
AttributeError: 'Canvas' object has no attribute 'set_focus'
>>> root.set_focus(canv)
Traceback (most recent call last):
  File "<pyshell#363>", line 1, in <module>
    root.set_focus(canv)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1867, in __getattr__
    return getattr(self.tk, attr)
AttributeError: 'tkapp' object has no attribute 'set_focus'
>>> help(tkinter.set_focus)
Traceback (most recent call last):
  File "<pyshell#364>", line 1, in <module>
    help(tkinter.set_focus)
NameError: name 'tkinter' is not defined
>>> help(set_focus)
Traceback (most recent call last):
  File "<pyshell#365>", line 1, in <module>
    help(set_focus)
NameError: name 'set_focus' is not defined
>>> help(Tk.set_focus)
Traceback (most recent call last):
  File "<pyshell#366>", line 1, in <module>
    help(Tk.set_focus)
AttributeError: type object 'Tk' has no attribute 'set_focus'
>>> help(Canvas.set_focus)
Traceback (most recent call last):
  File "<pyshell#367>", line 1, in <module>
    help(Canvas.set_focus)
AttributeError: type object 'Canvas' has no attribute 'set_focus'
>>> canv.find_withtag("icon")
()
>>> create_icons(canv, list_of_icon_coords)
Traceback (most recent call last):
  File "<pyshell#369>", line 1, in <module>
    create_icons(canv, list_of_icon_coords)
  File "<pyshell#354>", line 3, in create_icons
    canvas_item.create_rectangle(item[0], item[1], item[2], item[3], fill='', outline='blue', tags='icon', highlightcolor='red' )
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2331, in create_rectangle
    return self._create('rectangle', args, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2310, in _create
    *(args + self._options(cnf, kw))))
_tkinter.TclError: unknown option "-highlightcolor"
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 121, in main
    seq, request = rpc.request_queue.get(block=True, timeout=0.05)
  File "C:\Python33x86\lib\queue.py", line 175, in get
    raise Empty
queue.Empty

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\tkinter\__init__.py", line 1475, in __call__
    return self.func(*args)
  File "<pyshell#100>", line 1, in <lambda>
  File "<pyshell#358>", line 2, in on_motion
NameError: global name 'set_focus' is not defined
def on_motion(event, coords_list):
	current = canv.find_withtag('current')
	closest = canv.find_closest(event.x, event.y, 1)
	loc = (event.x, event.y, current)
	lbl.configure(text=loc)
	canv.focus(closest)

	try:
		if 'icon' in current:
			print("Closest, Current:", closest, current)
			selected = closest
			canv.focus(selected)
		#else:
			#canv.itemconfig(closest, outline='blue')
	except TclError:
		print("ERROR: ", closest, canv.gettags(closest))


	#for item in coords_list:
		#if (loc[0] >= item[0] and loc[0] <= item[2]) and (loc[1] >= item[1] and loc[1] <= item[3]):
			#canv.create_rectangle(item[0], item[1], item[2]+1, item[3]+1, outline='red')

		
>>> def create_icons(canvas_item, list_of_icon_coords):
	for item in list_of_icon_coords:
		canvas_item.create_rectangle(item[0], item[1], item[2], item[3], fill='', outline='blue', tags='icon', activeoutline='green', outline='blue', fill='#FFFFFFFF' )
		
SyntaxError: keyword argument repeated
>>> 
>>> def create_icons(canvas_item, list_of_icon_coords):
	for item in list_of_icon_coords:
		canvas_item.create_rectangle(item[0], item[1], item[2], item[3], fill='', tags='icon', activeoutline='green', outline='blue', fill='#FFFFFFFF' )
		
SyntaxError: keyword argument repeated
>>> def create_icons(canvas_item, list_of_icon_coords):
	for item in list_of_icon_coords:
		canvas_item.create_rectangle(item[0], item[1], item[2], item[3], tags='icon', activeoutline='green', outline='blue', fill='#FFFFFFFF' )

		
>>> create_icons(canv, list_of_icon_coords)
Traceback (most recent call last):
  File "<pyshell#377>", line 1, in <module>
    create_icons(canv, list_of_icon_coords)
  File "<pyshell#376>", line 3, in create_icons
    canvas_item.create_rectangle(item[0], item[1], item[2], item[3], tags='icon', activeoutline='green', outline='blue', fill='#FFFFFFFF' )
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2331, in create_rectangle
    return self._create('rectangle', args, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2310, in _create
    *(args + self._options(cnf, kw))))
_tkinter.TclError: invalid color name "#FFFFFFFF"
>>> def create_icons(canvas_item, list_of_icon_coords):
	for item in list_of_icon_coords:
		canvas_item.create_rectangle(item[0], item[1], item[2], item[3], tags='icon', activeoutline='green', outline='blue', fill='#FFFFFF' )

		
>>> create_icons(canv, list_of_icon_coords)
>>> def create_icons(canvas_item, list_of_icon_coords):
	for item in list_of_icon_coords:
		canvas_item.create_rectangle(item[0], item[1], item[2], item[3], tags='icon', activeoutline='green', outline='blue', fill='rgb(255, 255, 255)' )

		
>>> create_icons(canv, list_of_icon_coords)
Traceback (most recent call last):
  File "<pyshell#383>", line 1, in <module>
    create_icons(canv, list_of_icon_coords)
  File "<pyshell#382>", line 3, in create_icons
    canvas_item.create_rectangle(item[0], item[1], item[2], item[3], tags='icon', activeoutline='green', outline='blue', fill='rgb(255, 255, 255)' )
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2331, in create_rectangle
    return self._create('rectangle', args, kw)
  File "C:\Python33x86\lib\tkinter\__init__.py", line 2310, in _create
    *(args + self._options(cnf, kw))))
_tkinter.TclError: unknown color name "rgb(255, 255, 255)"
>>> def create_icons(canvas_item, list_of_icon_coords):
	for item in list_of_icon_coords:
		canvas_item.create_rectangle(item[0], item[1], item[2], item[3], tags='icon', activeoutline='green', outline='blue', stipple='gray50' )

		
>>> delete_icons(canv)
>>> create_icons(canv, list_of_icon_coords)
>>> delete_icons(canv)
>>> def create_icons(canvas_item, list_of_icon_coords):
	for item in list_of_icon_coords:
		canvas_item.create_rectangle(item[0], item[1], item[2], item[3], tags='icon', activeoutline='green', outline='blue', fill='gray50' )

		
>>> create_icons(canv, list_of_icon_coords)
>>> 
>>> def create_icons(canvas_item, list_of_icon_coords):
	for item in list_of_icon_coords:
		canvas_item.create_rectangle(item[0], item[1], item[2], item[3], tags='icon', activeoutline='green', outline='blue', fill='gray99' )

		
>>> delete_icons(canv)
>>> create_icons(canv, list_of_icon_coords)
>>> delete_icons(canv)
>>> icon_map = PeriodicCoordinateMap()
>>> list_of_icon_coords = icon_map.getIconCoords()
>>> list_of_icon_coords.clear()
>>> list_of_icon_coords = icon_map.getIconCoords()
>>> create_icons(canv, list_of_icon_coords)
>>> import PeriodicCoordinateMap()
SyntaxError: invalid syntax
>>> import PeriodicCoordinateMap
>>> list_of_icon_coords.clear()
>>> icon_map = PeriodicCoordinateMap()
Traceback (most recent call last):
  File "<pyshell#406>", line 1, in <module>
    icon_map = PeriodicCoordinateMap()
TypeError: 'module' object is not callable
>>> icon_map = PeriodicCoordinateMap()
Traceback (most recent call last):
  File "<pyshell#407>", line 1, in <module>
    icon_map = PeriodicCoordinateMap()
TypeError: 'module' object is not callable
>>> from PeriodicCoordinateMap import *
>>> icon_map = PeriodicCoordinateMap()
>>> list_of_icon_coords = icon_map.getIconCoords()
>>> delete_icons(canv)
>>> create_icons(canv, list_of_icon_coords)
>>> imp.reload(PeriodicCoordinateMap)
Traceback (most recent call last):
  File "<pyshell#413>", line 1, in <module>
    imp.reload(PeriodicCoordinateMap)
NameError: name 'imp' is not defined
>>> import imp
>>> imp.reload(PeriodicCoordinateMap)
Traceback (most recent call last):
  File "<pyshell#415>", line 1, in <module>
    imp.reload(PeriodicCoordinateMap)
  File "C:\Python33x86\lib\imp.py", line 263, in reload
    raise TypeError("reload() argument must be module")
TypeError: reload() argument must be module
>>> imp.reload(from PeriodicCoordinateMap *)
SyntaxError: invalid syntax
>>> help(imp)
Help on module imp:

NAME
    imp

MODULE REFERENCE
    http://docs.python.org/3.3/library/imp
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides the components needed to build your own __import__
    function.  Undocumented functions are obsolete.
    
    In most cases it is preferred you consider using the importlib module's
    functionality over this module.

CLASSES
    builtins.object
        NullImporter
    
    class NullImporter(builtins.object)
     |  Null import object.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, path)
     |  
     |  find_module(self, fullname)
     |      Always returns None.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    acquire_lock(...)
        acquire_lock() -> None
        Acquires the interpreter's import lock for the current thread.
        This lock should be used by import hooks to ensure thread-safety
        when importing modules.
        On platforms without threads, this function does nothing.
    
    find_module(name, path=None)
        **DEPRECATED**
        
        Search for a module.
        
        If path is omitted or None, search for a built-in, frozen or special
        module and continue search in sys.path. The module name cannot
        contain '.'; to search for a submodule of a package, pass the
        submodule name and the package's __path__.
    
    get_frozen_object(...)
    
    get_magic()
        Return the magic number for .pyc or .pyo files.
    
    get_suffixes()
    
    get_tag()
        Return the magic tag for .pyc or .pyo files.
    
    init_builtin(...)
    
    init_frozen(...)
    
    is_builtin(...)
    
    is_frozen(...)
    
    is_frozen_package(...)
    
    load_compiled(name, pathname, file=None)
    
    load_dynamic(...)
    
    load_module(name, file, filename, details)
        **DEPRECATED**
        
        Load a module, given information returned by find_module().
        
        The module name must include the full package name, if any.
    
    load_package(name, path)
    
    load_source(name, pathname, file=None)
    
    lock_held(...)
        lock_held() -> boolean
        Return True if the import lock is currently held, else False.
        On platforms without threads, return False.
    
    release_lock(...)
        release_lock() -> None
        Release the interpreter's import lock.
        On platforms without threads, this function does nothing.
    
    reload(module)
        Reload the module and return it.
        
        The module must have been successfully imported before.

DATA
    C_BUILTIN = 6
    C_EXTENSION = 3
    IMP_HOOK = 9
    PKG_DIRECTORY = 5
    PY_CODERESOURCE = 8
    PY_COMPILED = 2
    PY_FROZEN = 7
    PY_RESOURCE = 4
    PY_SOURCE = 1
    SEARCH_ERROR = 0
    __warningregistry__ = {('imp.get_suffixes() is deprecated; use the con...

FILE
    c:\python33x86\lib\imp.py


>>> imp.reload(PeriodicCoordinateMap.getIconCoords)
Traceback (most recent call last):
  File "<pyshell#418>", line 1, in <module>
    imp.reload(PeriodicCoordinateMap.getIconCoords)
  File "C:\Python33x86\lib\imp.py", line 263, in reload
    raise TypeError("reload() argument must be module")
TypeError: reload() argument must be module
>>> imp.reload(PeriodicCoordinateMap.getIconCoords())
Traceback (most recent call last):
  File "<pyshell#419>", line 1, in <module>
    imp.reload(PeriodicCoordinateMap.getIconCoords())
TypeError: getIconCoords() missing 1 required positional argument: 'self'
>>> imp.reload(PeriodicCoordinateMap.getIconCoords)
Traceback (most recent call last):
  File "<pyshell#420>", line 1, in <module>
    imp.reload(PeriodicCoordinateMap.getIconCoords)
  File "C:\Python33x86\lib\imp.py", line 263, in reload
    raise TypeError("reload() argument must be module")
TypeError: reload() argument must be module
>>> imp.reload(getIconCoords)
Traceback (most recent call last):
  File "<pyshell#421>", line 1, in <module>
    imp.reload(getIconCoords)
NameError: name 'getIconCoords' is not defined
>>> from PeriodicCoordinateMap imp.reload(*)
SyntaxError: invalid syntax
>>> from PeriodicCoordinateMap import * as frump
SyntaxError: invalid syntax
>>> from PeriodicCoordinateMap import getIconCoords
Traceback (most recent call last):
  File "<pyshell#424>", line 1, in <module>
    from PeriodicCoordinateMap import getIconCoords
ImportError: cannot import name getIconCoords
>>> from PeriodicCoordinateMap import getIconCoords()
SyntaxError: invalid syntax
>>> from PeriodicCoordinateMap import getIconCoords
Traceback (most recent call last):
  File "<pyshell#426>", line 1, in <module>
    from PeriodicCoordinateMap import getIconCoords
ImportError: cannot import name getIconCoords
>>> help(imp)
Help on module imp:

NAME
    imp

MODULE REFERENCE
    http://docs.python.org/3.3/library/imp
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides the components needed to build your own __import__
    function.  Undocumented functions are obsolete.
    
    In most cases it is preferred you consider using the importlib module's
    functionality over this module.

CLASSES
    builtins.object
        NullImporter
    
    class NullImporter(builtins.object)
     |  Null import object.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, path)
     |  
     |  find_module(self, fullname)
     |      Always returns None.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    acquire_lock(...)
        acquire_lock() -> None
        Acquires the interpreter's import lock for the current thread.
        This lock should be used by import hooks to ensure thread-safety
        when importing modules.
        On platforms without threads, this function does nothing.
    
    find_module(name, path=None)
        **DEPRECATED**
        
        Search for a module.
        
        If path is omitted or None, search for a built-in, frozen or special
        module and continue search in sys.path. The module name cannot
        contain '.'; to search for a submodule of a package, pass the
        submodule name and the package's __path__.
    
    get_frozen_object(...)
    
    get_magic()
        Return the magic number for .pyc or .pyo files.
    
    get_suffixes()
    
    get_tag()
        Return the magic tag for .pyc or .pyo files.
    
    init_builtin(...)
    
    init_frozen(...)
    
    is_builtin(...)
    
    is_frozen(...)
    
    is_frozen_package(...)
    
    load_compiled(name, pathname, file=None)
    
    load_dynamic(...)
    
    load_module(name, file, filename, details)
        **DEPRECATED**
        
        Load a module, given information returned by find_module().
        
        The module name must include the full package name, if any.
    
    load_package(name, path)
    
    load_source(name, pathname, file=None)
    
    lock_held(...)
        lock_held() -> boolean
        Return True if the import lock is currently held, else False.
        On platforms without threads, return False.
    
    release_lock(...)
        release_lock() -> None
        Release the interpreter's import lock.
        On platforms without threads, this function does nothing.
    
    reload(module)
        Reload the module and return it.
        
        The module must have been successfully imported before.

DATA
    C_BUILTIN = 6
    C_EXTENSION = 3
    IMP_HOOK = 9
    PKG_DIRECTORY = 5
    PY_CODERESOURCE = 8
    PY_COMPILED = 2
    PY_FROZEN = 7
    PY_RESOURCE = 4
    PY_SOURCE = 1
    SEARCH_ERROR = 0
    __warningregistry__ = {('imp.get_suffixes() is deprecated; use the con...

FILE
    c:\python33x86\lib\imp.py


>>> imp.load_package(PeriodicCoordinateMap, 'c:\\users\\compy\\documents\\github\\pythonlearning\\')
Traceback (most recent call last):
  File "<pyshell#428>", line 1, in <module>
    imp.load_package(PeriodicCoordinateMap, 'c:\\users\\compy\\documents\\github\\pythonlearning\\')
  File "C:\Python33x86\lib\imp.py", line 159, in load_package
    raise ValueError('{!r} is not a package'.format(path))
ValueError: 'c:\\users\\compy\\documents\\github\\pythonlearning\\__init__.py\\__init__.pyw\\__init__.pyc' is not a package
>>> imp.load_source(PeriodicCoordinateMap, 'c:\\users\\compy\\documents\\github\\pythonlearning\\', PeriodicCoordinateMap.py)
Traceback (most recent call last):
  File "<pyshell#429>", line 1, in <module>
    imp.load_source(PeriodicCoordinateMap, 'c:\\users\\compy\\documents\\github\\pythonlearning\\', PeriodicCoordinateMap.py)
AttributeError: type object 'PeriodicCoordinateMap' has no attribute 'py'
>>> imp.load_source(PeriodicCoordinateMap, 'c:\\users\\compy\\documents\\github\\pythonlearning\\', PeriodicCoordinateMap)
Traceback (most recent call last):
  File "<pyshell#430>", line 1, in <module>
    imp.load_source(PeriodicCoordinateMap, 'c:\\users\\compy\\documents\\github\\pythonlearning\\', PeriodicCoordinateMap)
  File "C:\Python33x86\lib\imp.py", line 119, in load_source
    _LoadSourceCompatibility(name, pathname, file).load_module(name)
  File "<frozen importlib._bootstrap>", line 584, in _check_name_wrapper
  File "<frozen importlib._bootstrap>", line 1022, in load_module
  File "<frozen importlib._bootstrap>", line 1003, in load_module
  File "<frozen importlib._bootstrap>", line 541, in module_for_loader_wrapper
  File "<frozen importlib._bootstrap>", line 160, in new_module
TypeError: module.__init__() argument 1 must be str, not type
>>> help(imp)
Help on module imp:

NAME
    imp

MODULE REFERENCE
    http://docs.python.org/3.3/library/imp
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides the components needed to build your own __import__
    function.  Undocumented functions are obsolete.
    
    In most cases it is preferred you consider using the importlib module's
    functionality over this module.

CLASSES
    builtins.object
        NullImporter
    
    class NullImporter(builtins.object)
     |  Null import object.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, path)
     |  
     |  find_module(self, fullname)
     |      Always returns None.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    acquire_lock(...)
        acquire_lock() -> None
        Acquires the interpreter's import lock for the current thread.
        This lock should be used by import hooks to ensure thread-safety
        when importing modules.
        On platforms without threads, this function does nothing.
    
    find_module(name, path=None)
        **DEPRECATED**
        
        Search for a module.
        
        If path is omitted or None, search for a built-in, frozen or special
        module and continue search in sys.path. The module name cannot
        contain '.'; to search for a submodule of a package, pass the
        submodule name and the package's __path__.
    
    get_frozen_object(...)
    
    get_magic()
        Return the magic number for .pyc or .pyo files.
    
    get_suffixes()
    
    get_tag()
        Return the magic tag for .pyc or .pyo files.
    
    init_builtin(...)
    
    init_frozen(...)
    
    is_builtin(...)
    
    is_frozen(...)
    
    is_frozen_package(...)
    
    load_compiled(name, pathname, file=None)
    
    load_dynamic(...)
    
    load_module(name, file, filename, details)
        **DEPRECATED**
        
        Load a module, given information returned by find_module().
        
        The module name must include the full package name, if any.
    
    load_package(name, path)
    
    load_source(name, pathname, file=None)
    
    lock_held(...)
        lock_held() -> boolean
        Return True if the import lock is currently held, else False.
        On platforms without threads, return False.
    
    release_lock(...)
        release_lock() -> None
        Release the interpreter's import lock.
        On platforms without threads, this function does nothing.
    
    reload(module)
        Reload the module and return it.
        
        The module must have been successfully imported before.

DATA
    C_BUILTIN = 6
    C_EXTENSION = 3
    IMP_HOOK = 9
    PKG_DIRECTORY = 5
    PY_CODERESOURCE = 8
    PY_COMPILED = 2
    PY_FROZEN = 7
    PY_RESOURCE = 4
    PY_SOURCE = 1
    SEARCH_ERROR = 0
    __warningregistry__ = {('imp.get_suffixes() is deprecated; use the con...

FILE
    c:\python33x86\lib\imp.py


>>> from PeriodicCoordinateMap
SyntaxError: invalid syntax
>>> from PeriodicCoordinateMap import
SyntaxError: invalid syntax
>>> from PeriodicCoordinateMap import *
>>> sys.getrefcount(PeriodicCoordinateMap)
16
>>> sys.modules.values()
dict_values([<module 'importlib' from 'C:\\Python33x86\\lib\\importlib\\__init__.py'>, <module 'heapq' from 'C:\\Python33x86\\lib\\heapq.py'>, <module 'configparser' from 'C:\\Python33x86\\lib\\configparser.py'>, <module 'idlelib.RemoteObjectBrowser' from 'C:\\Python33x86\\lib\\idlelib\\RemoteObjectBrowser.py'>, <module 'encodings.latin_1' from 'C:\\Python33x86\\lib\\encodings\\latin_1.py'>, <module '_sre' (built-in)>, <module 'idlelib.macosxSupport' from 'C:\\Python33x86\\lib\\idlelib\\macosxSupport.py'>, <module 'sys' (built-in)>, <module '_hashlib' from 'C:\\Python33x86\\DLLs\\_hashlib.pyd'>, <module 'itertools' (built-in)>, <module 'warnings' from 'C:\\Python33x86\\lib\\warnings.py'>, <module 'os' from 'C:\\Python33x86\\lib\\os.py'>, <module 'zipimport' (built-in)>, <module 'encodings.aliases' from 'C:\\Python33x86\\lib\\encodings\\aliases.py'>, <module '_tkinter' from 'C:\\Python33x86\\DLLs\\_tkinter.pyd'>, <module 'abc' from 'C:\\Python33x86\\lib\\abc.py'>, <module 'struct' from 'C:\\Python33x86\\lib\\struct.py'>, <module 'io' (built-in)>, <module 'token' from 'C:\\Python33x86\\lib\\token.py'>, <module 'idlelib.idlever' from 'C:\\Python33x86\\lib\\idlelib\\idlever.py'>, <module 'idlelib.WidgetRedirector' from 'C:\\Python33x86\\lib\\idlelib\\WidgetRedirector.py'>, <module 'stat' from 'C:\\Python33x86\\lib\\stat.py'>, <module 'gc' (built-in)>, <module 'sre_compile' from 'C:\\Python33x86\\lib\\sre_compile.py'>, <module '_pickle' (built-in)>, <module 'copy' from 'C:\\Python33x86\\lib\\copy.py'>, <module 'idlelib.ReplaceDialog' from 'C:\\Python33x86\\lib\\idlelib\\ReplaceDialog.py'>, <module 'unicodedata' from 'C:\\Python33x86\\DLLs\\unicodedata.pyd'>, <module 'idlelib.rpc' from 'C:\\Python33x86\\lib\\idlelib\\rpc.py'>, <module '__main__' (built-in)>, <module '_socket' from 'C:\\Python33x86\\DLLs\\_socket.pyd'>, <module 'idlelib.aboutDialog' from 'C:\\Python33x86\\lib\\idlelib\\aboutDialog.py'>, <module 'hashlib' from 'C:\\Python33x86\\lib\\hashlib.py'>, <module 'queue' from 'C:\\Python33x86\\lib\\queue.py'>, <module 'idlelib.ZoomHeight' from 'C:\\Python33x86\\lib\\idlelib\\ZoomHeight.py'>, <module 'code' from 'C:\\Python33x86\\lib\\code.py'>, <module 'shlex' from 'C:\\Python33x86\\lib\\shlex.py'>, <module '_functools' (built-in)>, <module 'encodings.utf_8' from 'C:\\Python33x86\\lib\\encodings\\utf_8.py'>, <module '_imp' (built-in)>, <module 'swig_runtime_data4'>, <module 'PIL._binary' from 'C:\\Python33x86\\lib\\site-packages\\PIL\\_binary.py'>, <module 'encodings.cp1252' from 'C:\\Python33x86\\lib\\encodings\\cp1252.py'>, <module 'idlelib.Delegator' from 'C:\\Python33x86\\lib\\idlelib\\Delegator.py'>, <module 'PeriodicCoordinateMap' from 'c:\\users\\compy\\documents\\github\\pythonlearning\\PeriodicCoordinateMap.py'>, <module 'numbers' from 'C:\\Python33x86\\lib\\numbers.py'>, <module 'linecache' from 'C:\\Python33x86\\lib\\linecache.py'>, <module 'pydoc' from 'C:\\Python33x86\\lib\\pydoc.py'>, <module 'idlelib.FileList' from 'C:\\Python33x86\\lib\\idlelib\\FileList.py'>, <module 'pickle' from 'C:\\Python33x86\\lib\\pickle.py'>, <module 'zlib' (built-in)>, <module 'bdb' from 'C:\\Python33x86\\lib\\bdb.py'>, <module 'idlelib.TreeWidget' from 'C:\\Python33x86\\lib\\idlelib\\TreeWidget.py'>, <module 'collections.abc' from 'C:\\Python33x86\\lib\\collections\\abc.py'>, <module 'tokenize' from 'C:\\Python33x86\\lib\\tokenize.py'>, <module 'idlelib.SearchDialog' from 'C:\\Python33x86\\lib\\idlelib\\SearchDialog.py'>, <module 'idlelib.CallTipWindow' from 'C:\\Python33x86\\lib\\idlelib\\CallTipWindow.py'>, <module 'subprocess' from 'C:\\Python33x86\\lib\\subprocess.py'>, <module 'tkinter.font' from 'C:\\Python33x86\\lib\\tkinter\\font.py'>, <module 'io' from 'C:\\Python33x86\\lib\\io.py'>, <module 'idlelib.keybindingDialog' from 'C:\\Python33x86\\lib\\idlelib\\keybindingDialog.py'>, <module 'importlib._bootstrap' (frozen)>, <module 'ctypes._endian' from 'C:\\Python33x86\\lib\\ctypes\\_endian.py'>, <module 'types' from 'C:\\Python33x86\\lib\\types.py'>, <module '_openbabel' from 'C:\\Python33x86\\lib\\site-packages\\_openbabel.pyd'>, <module 'copyreg' from 'C:\\Python33x86\\lib\\copyreg.py'>, <module 'collections' from 'C:\\Python33x86\\lib\\collections\\__init__.py'>, <module 'encodings.cp437' from 'C:\\Python33x86\\lib\\encodings\\cp437.py'>, <module 'socket' from 'C:\\Python33x86\\lib\\socket.py'>, <module 'inspect' from 'C:\\Python33x86\\lib\\inspect.py'>, <module '_compat_pickle' from 'C:\\Python33x86\\lib\\_compat_pickle.py'>, <module '_locale' (built-in)>, <module 'opcode' from 'C:\\Python33x86\\lib\\opcode.py'>, <module 'sysconfig' from 'C:\\Python33x86\\lib\\sysconfig.py'>, <module 'ntpath' from 'C:\\Python33x86\\lib\\ntpath.py'>, <module 'idlelib.OutputWindow' from 'C:\\Python33x86\\lib\\idlelib\\OutputWindow.py'>, <module 'idlelib.IOBinding' from 'C:\\Python33x86\\lib\\idlelib\\IOBinding.py'>, <module 'genericpath' from 'C:\\Python33x86\\lib\\genericpath.py'>, <module 'codecs' from 'C:\\Python33x86\\lib\\codecs.py'>, <module 'nt' (built-in)>, <module 'idlelib.SearchEngine' from 'C:\\Python33x86\\lib\\idlelib\\SearchEngine.py'>, <module 'ctypes' from 'C:\\Python33x86\\lib\\ctypes\\__init__.py'>, <module 'site' from 'C:\\Python33x86\\lib\\site.py'>, <module 'idlelib.MultiCall' from 'C:\\Python33x86\\lib\\idlelib\\MultiCall.py'>, <module '_codecs' (built-in)>, <module 'winreg' (built-in)>, <module 'idlelib.EditorWindow' from 'C:\\Python33x86\\lib\\idlelib\\EditorWindow.py'>, <module 'idlelib.ObjectBrowser' from 'C:\\Python33x86\\lib\\idlelib\\ObjectBrowser.py'>, <module 'idlelib.MultiStatusBar' from 'C:\\Python33x86\\lib\\idlelib\\MultiStatusBar.py'>, <module 'idlelib.RemoteDebugger' from 'C:\\Python33x86\\lib\\idlelib\\RemoteDebugger.py'>, <module 'sre_constants' from 'C:\\Python33x86\\lib\\sre_constants.py'>, <module 'PIL.Image' from 'C:\\Python33x86\\lib\\site-packages\\PIL\\Image.py'>, <module 'idlelib.configDialog' from 'C:\\Python33x86\\lib\\idlelib\\configDialog.py'>, <module 'idlelib.configHandler' from 'C:\\Python33x86\\lib\\idlelib\\configHandler.py'>, <module 'platform' from 'C:\\Python33x86\\lib\\platform.py'>, <module '_struct' (built-in)>, <module 'tkinter.constants' from 'C:\\Python33x86\\lib\\tkinter\\constants.py'>, <module 'idlelib.HyperParser' from 'C:\\Python33x86\\lib\\idlelib\\HyperParser.py'>, <module 'idlelib.PyShell' from 'C:\\Python33x86\\lib\\idlelib\\PyShell.py'>, <module 'tkinter.commondialog' from 'C:\\Python33x86\\lib\\tkinter\\commondialog.py'>, <module 'string' from 'C:\\Python33x86\\lib\\string.py'>, <module '_winapi' (built-in)>, <module 'weakref' from 'C:\\Python33x86\\lib\\weakref.py'>, <module '_collections' (built-in)>, <module 'locale' from 'C:\\Python33x86\\lib\\locale.py'>, <module 'idlelib.textView' from 'C:\\Python33x86\\lib\\idlelib\\textView.py'>, <module 'reprlib' from 'C:\\Python33x86\\lib\\reprlib.py'>, <module '_heapq' (built-in)>, <module 'PIL._imaging' from 'C:\\Python33x86\\lib\\site-packages\\PIL\\_imaging.pyd'>, <module 're' from 'C:\\Python33x86\\lib\\re.py'>, <module '_weakrefset' from 'C:\\Python33x86\\lib\\_weakrefset.py'>, <module 'PIL' from 'C:\\Python33x86\\lib\\site-packages\\PIL\\__init__.py'>, <module 'signal' (built-in)>, <module '_thread' (built-in)>, <module 'importlib.abc' from 'C:\\Python33x86\\lib\\importlib\\abc.py'>, <module 'threading' from 'C:\\Python33x86\\lib\\threading.py'>, <module 'PIL.ImageTk' from 'C:\\Python33x86\\lib\\site-packages\\PIL\\ImageTk.py'>, <module 'idlelib.run' from 'C:\\Python33x86\\lib\\idlelib\\run.py'>, <module 'fnmatch' from 'C:\\Python33x86\\lib\\fnmatch.py'>, <module 'webbrowser' from 'C:\\Python33x86\\lib\\webbrowser.py'>, <module 'pybel' from 'C:\\Python33x86\\lib\\site-packages\\pybel.py'>, <module 'tkinter.messagebox' from 'C:\\Python33x86\\lib\\tkinter\\messagebox.py'>, <module 'imp' from 'C:\\Python33x86\\lib\\imp.py'>, <module '__future__' from 'C:\\Python33x86\\lib\\__future__.py'>, <module 'openbabel' from 'C:\\Python33x86\\lib\\site-packages\\openbabel.py'>, <module '_string' (built-in)>, <module 'idlelib.CallTips' from 'C:\\Python33x86\\lib\\idlelib\\CallTips.py'>, <module 'msvcrt' (built-in)>, <module 'ntpath' from 'C:\\Python33x86\\lib\\ntpath.py'>, <module 'posixpath' from 'C:\\Python33x86\\lib\\posixpath.py'>, <module 'builtins' (built-in)>, <module 'encodings.mbcs' from 'C:\\Python33x86\\lib\\encodings\\mbcs.py'>, <module 'idlelib.Debugger' from 'C:\\Python33x86\\lib\\idlelib\\Debugger.py'>, <module 'idlelib.ScrolledList' from 'C:\\Python33x86\\lib\\idlelib\\ScrolledList.py'>, <module 'idlelib.SearchDialogBase' from 'C:\\Python33x86\\lib\\idlelib\\SearchDialogBase.py'>, <module 'importlib._bootstrap' (frozen)>, <module 'array' (built-in)>, <module 'idlelib' from 'C:\\Python33x86\\lib\\idlelib\\__init__.py'>, <module 'importlib.machinery' from 'C:\\Python33x86\\lib\\importlib\\machinery.py'>, <module 'idlelib.Percolator' from 'C:\\Python33x86\\lib\\idlelib\\Percolator.py'>, <module 'idlelib.AutoComplete' from 'C:\\Python33x86\\lib\\idlelib\\AutoComplete.py'>, <module 'socketserver' from 'C:\\Python33x86\\lib\\socketserver.py'>, <module '_ctypes' from 'C:\\Python33x86\\DLLs\\_ctypes.pyd'>, <module 'tkinter' from 'C:\\Python33x86\\lib\\tkinter\\__init__.py'>, <module 'idlelib.IdleHistory' from 'C:\\Python33x86\\lib\\idlelib\\IdleHistory.py'>, <module 'idlelib.ColorDelegator' from 'C:\\Python33x86\\lib\\idlelib\\ColorDelegator.py'>, <module 'tempfile' from 'C:\\Python33x86\\lib\\tempfile.py'>, <module 'idlelib.WindowList' from 'C:\\Python33x86\\lib\\idlelib\\WindowList.py'>, <module 'PIL.ImageMode' from 'C:\\Python33x86\\lib\\site-packages\\PIL\\ImageMode.py'>, <module '_weakref' (built-in)>, <module 'operator' (built-in)>, <module 'idlelib.GrepDialog' from 'C:\\Python33x86\\lib\\idlelib\\GrepDialog.py'>, <module 'functools' from 'C:\\Python33x86\\lib\\functools.py'>, <module 'tkinter.ttk' from 'C:\\Python33x86\\lib\\tkinter\\ttk.py'>, <module 'gettext' from 'C:\\Python33x86\\lib\\gettext.py'>, <module '_warnings' (built-in)>, <module 'pkgutil' from 'C:\\Python33x86\\lib\\pkgutil.py'>, <module 'keyword' from 'C:\\Python33x86\\lib\\keyword.py'>, <module 'tkinter.simpledialog' from 'C:\\Python33x86\\lib\\tkinter\\simpledialog.py'>, <module 'math' (built-in)>, <module 'idlelib.PyParse' from 'C:\\Python33x86\\lib\\idlelib\\PyParse.py'>, <module 'idlelib.dynOptionMenuWidget' from 'C:\\Python33x86\\lib\\idlelib\\dynOptionMenuWidget.py'>, <module 'errno' (built-in)>, <module 'idlelib.configHelpSourceEdit' from 'C:\\Python33x86\\lib\\idlelib\\configHelpSourceEdit.py'>, <module 'tkinter.colorchooser' from 'C:\\Python33x86\\lib\\tkinter\\colorchooser.py'>, <module 'sre_parse' from 'C:\\Python33x86\\lib\\sre_parse.py'>, <module 'tkinter.dialog' from 'C:\\Python33x86\\lib\\tkinter\\dialog.py'>, <module 'idlelib.configSectionNameDialog' from 'C:\\Python33x86\\lib\\idlelib\\configSectionNameDialog.py'>, <module 'time' (built-in)>, <module 'encodings' from 'C:\\Python33x86\\lib\\encodings\\__init__.py'>, <module 'idlelib.Bindings' from 'C:\\Python33x86\\lib\\idlelib\\Bindings.py'>, <module 'stringprep' from 'C:\\Python33x86\\lib\\stringprep.py'>, <module 'PIL._util' from 'C:\\Python33x86\\lib\\site-packages\\PIL\\_util.py'>, <module 'traceback' from 'C:\\Python33x86\\lib\\traceback.py'>, <module 'idlelib.StackViewer' from 'C:\\Python33x86\\lib\\idlelib\\StackViewer.py'>, <module 'idlelib.AutoCompleteWindow' from 'C:\\Python33x86\\lib\\idlelib\\AutoCompleteWindow.py'>, <module 'codeop' from 'C:\\Python33x86\\lib\\codeop.py'>, <module 'idlelib.UndoDelegator' from 'C:\\Python33x86\\lib\\idlelib\\UndoDelegator.py'>, <module 'select' from 'C:\\Python33x86\\DLLs\\select.pyd'>, <module 'getopt' from 'C:\\Python33x86\\lib\\getopt.py'>, <module 'tkinter.filedialog' from 'C:\\Python33x86\\lib\\tkinter\\filedialog.py'>, <module 'dis' from 'C:\\Python33x86\\lib\\dis.py'>, <module 'encodings.idna' from 'C:\\Python33x86\\lib\\encodings\\idna.py'>, <module 'idlelib.tabbedpages' from 'C:\\Python33x86\\lib\\idlelib\\tabbedpages.py'>, <module 'marshal' (built-in)>, <module 'random' from 'C:\\Python33x86\\lib\\random.py'>, <module 'tkinter._fix' from 'C:\\Python33x86\\lib\\tkinter\\_fix.py'>, <module '_random' (built-in)>])
>>> for mod in sys.modules.values():
	imp.reload(mod)

	
<module 'importlib' from 'C:\\Python33x86\\lib\\importlib\\__init__.py'>
<module 'heapq' from 'C:\\Python33x86\\lib\\heapq.py'>
<module 'configparser' from 'C:\\Python33x86\\lib\\configparser.py'>
<module 'idlelib.RemoteObjectBrowser' from 'C:\\Python33x86\\lib\\idlelib\\RemoteObjectBrowser.py'>
<module 'encodings.latin_1' from 'C:\\Python33x86\\lib\\encodings\\latin_1.py'>
<module '_sre' (built-in)>
<module 'idlelib.macosxSupport' from 'C:\\Python33x86\\lib\\idlelib\\macosxSupport.py'>
<module 'sys' (built-in)>
<module '_hashlib' from 'C:\\Python33x86\\DLLs\\_hashlib.pyd'>
<module 'itertools' (built-in)>
<module 'warnings' from 'C:\\Python33x86\\lib\\warnings.py'>
<module 'os' from 'C:\\Python33x86\\lib\\os.py'>
<module 'zipimport' (built-in)>
<module 'encodings.aliases' from 'C:\\Python33x86\\lib\\encodings\\aliases.py'>
<module '_tkinter' from 'C:\\Python33x86\\DLLs\\_tkinter.pyd'>
<module 'abc' from 'C:\\Python33x86\\lib\\abc.py'>
<module 'struct' from 'C:\\Python33x86\\lib\\struct.py'>
Traceback (most recent call last):
  File "<pyshell#439>", line 2, in <module>
    imp.reload(mod)
  File "C:\Python33x86\lib\imp.py", line 276, in reload
    module.__loader__.load_module(name)
  File "<frozen importlib._bootstrap>", line 495, in set_package_wrapper
  File "<frozen importlib._bootstrap>", line 508, in set_loader_wrapper
  File "<frozen importlib._bootstrap>", line 594, in _requires_builtin_wrapper
ImportError: io is not a built-in module
>>> for mod in sys.modules.values():
	reload(mod)

	
Traceback (most recent call last):
  File "<pyshell#441>", line 2, in <module>
    reload(mod)
NameError: name 'reload' is not defined
>>> for mod in sys.modules.values():
	try:
		imp.reload(mod)
	except ImportError:
		pass

	
<module 'importlib' from 'C:\\Python33x86\\lib\\importlib\\__init__.py'>
<module 'heapq' from 'C:\\Python33x86\\lib\\heapq.py'>
<module 'configparser' from 'C:\\Python33x86\\lib\\configparser.py'>
<module 'idlelib.RemoteObjectBrowser' from 'C:\\Python33x86\\lib\\idlelib\\RemoteObjectBrowser.py'>
<module 'encodings.latin_1' from 'C:\\Python33x86\\lib\\encodings\\latin_1.py'>
<module '_sre' (built-in)>
<module 'idlelib.macosxSupport' from 'C:\\Python33x86\\lib\\idlelib\\macosxSupport.py'>
<module 'sys' (built-in)>
<module '_hashlib' from 'C:\\Python33x86\\DLLs\\_hashlib.pyd'>
<module 'itertools' (built-in)>
<module 'warnings' from 'C:\\Python33x86\\lib\\warnings.py'>
<module 'os' from 'C:\\Python33x86\\lib\\os.py'>
<module 'zipimport' (built-in)>
<module 'encodings.aliases' from 'C:\\Python33x86\\lib\\encodings\\aliases.py'>
<module '_tkinter' from 'C:\\Python33x86\\DLLs\\_tkinter.pyd'>
<module 'abc' from 'C:\\Python33x86\\lib\\abc.py'>
<module 'struct' from 'C:\\Python33x86\\lib\\struct.py'>
<module 'token' from 'C:\\Python33x86\\lib\\token.py'>
<module 'idlelib.idlever' from 'C:\\Python33x86\\lib\\idlelib\\idlever.py'>
<module 'idlelib.WidgetRedirector' from 'C:\\Python33x86\\lib\\idlelib\\WidgetRedirector.py'>
<module 'stat' from 'C:\\Python33x86\\lib\\stat.py'>
<module 'gc' (built-in)>
<module 'sre_compile' from 'C:\\Python33x86\\lib\\sre_compile.py'>
<module '_pickle' (built-in)>
<module 'copy' from 'C:\\Python33x86\\lib\\copy.py'>
<module 'idlelib.ReplaceDialog' from 'C:\\Python33x86\\lib\\idlelib\\ReplaceDialog.py'>
<module 'unicodedata' from 'C:\\Python33x86\\DLLs\\unicodedata.pyd'>
<module 'idlelib.rpc' from 'C:\\Python33x86\\lib\\idlelib\\rpc.py'>
<module '_socket' from 'C:\\Python33x86\\DLLs\\_socket.pyd'>
<module 'idlelib.aboutDialog' from 'C:\\Python33x86\\lib\\idlelib\\aboutDialog.py'>
<module 'hashlib' from 'C:\\Python33x86\\lib\\hashlib.py'>
<module 'queue' from 'C:\\Python33x86\\lib\\queue.py'>
<module 'idlelib.ZoomHeight' from 'C:\\Python33x86\\lib\\idlelib\\ZoomHeight.py'>
<module 'code' from 'C:\\Python33x86\\lib\\code.py'>
<module 'shlex' from 'C:\\Python33x86\\lib\\shlex.py'>
<module '_functools' (built-in)>
<module 'encodings.utf_8' from 'C:\\Python33x86\\lib\\encodings\\utf_8.py'>
<module '_imp' (built-in)>
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 353, in runcode
    exec(code, self.locals)
  File "<pyshell#446>", line 3, in <module>
  File "C:\Python33x86\lib\imp.py", line 276, in reload
    module.__loader__.load_module(name)
AttributeError: 'module' object has no attribute '__loader__'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python33x86\lib\idlelib\run.py", line 126, in main
    ret = method(*args, **kwargs)
  File "C:\Python33x86\lib\idlelib\run.py", line 365, in runcode
    print_exception()
  File "C:\Python33x86\lib\idlelib\run.py", line 216, in print_exception
    print_exc(typ, val, tb)
  File "C:\Python33x86\lib\idlelib\run.py", line 210, in print_exc
    cleanup_traceback(tbe, exclude)
  File "C:\Python33x86\lib\idlelib\run.py", line 239, in cleanup_traceback
    rpchandler = rpc.objecttable['exec'].rpchandler
KeyError: 'exec'

>>> ================================ RESTART ================================
>>> for mod in sys.modules.values():
	try:
		imp.reload(mod)
	except ImportError:
		pass
	except KeyError:
		pass

	
Traceback (most recent call last):
  File "<pyshell#450>", line 1, in <module>
    for mod in sys.modules.values():
NameError: name 'sys' is not defined
>>> sys.getrefcount(sys)
Traceback (most recent call last):
  File "<pyshell#451>", line 1, in <module>
    sys.getrefcount(sys)
NameError: name 'sys' is not defined
>>> import sys
>>> for mod in sys.modules.values():
	try:
		imp.reload(mod)
	except ImportError:
		pass
	except KeyError:
		pass

	
Traceback (most recent call last):
  File "<pyshell#454>", line 3, in <module>
    imp.reload(mod)
NameError: name 'imp' is not defined
>>> import imp
>>> 
>>> 
