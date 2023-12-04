from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Change_note import Change_note
from datetime import datetime, time , date , timedelta
from ...audit_history import audit_history
from .. import Lists
from ...Add_changes import add_change_note


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
      
    today = date.today()
    print (today)
    if self.type_textbox.text =='Safety':
        self.type_textbox.foreground = '#f56b6b'
        self.type_textbox.bold = True
    if self.text_box_1.text =='1. High Priority':
          self.text_box_1.foreground = '#f56b6b'
    elif  self.text_box_1.text == '2. Medium Priority':
          self.text_box_1.foreground = 'theme:Secondary 500'
    if self.text_box_3.text:
          duedate = datetime.strptime(self.text_box_3.text,"%d %b %Y")
          # print('Due_Date=', duedate)
          if duedate < datetime.today() : 
              self.text_box_3.foreground = '#f56b6b'
              self.text_box_3.bold = True
               
    # if self.item['pick']:
    #       self.pick_textbox.bold =True
    # Any code you write here will run before the form opens.
# EDIT
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    change_copy = dict(list(self.item))

    if change_copy['difficulty'] and change_copy['payoff']:
        self.item['ips'] = change_copy['difficulty']*change_copy['payoff']
    if change_copy['severity'] and  change_copy['probability'] and change_copy['visibility']:
        self.item['rpn']  =change_copy['severity'] * change_copy['probability'] * change_copy['visibility']
        self.item['priority'] =change_copy['priority']
    
    save_1_clicked = alert(
      content=Change_note(item=change_copy),
      title="Update Change Note",
      large=True,
      buttons=[]
    )
    # Update the change if the user clicks save
    if save_1_clicked:
      anvil.server.call('update_change_1', self.item, change_copy)
      # self.add_change_note()
      self.refresh_data_bindings()
      
    # change_copy = dict(list(self.item))

    # if change_copy['difficulty'] and change_copy['payoff']:
    #     self.item['ips'] = change_copy['difficulty']*change_copy['payoff']
    # if change_copy['severity'] and  change_copy['probability'] and change_copy['visibility']:
    #     self.item['rpn']  =change_copy['severity'] * change_copy['probability'] * change_copy['visibility']
    #     self.item['priority'] =change_copy['priority']
    # # open change note form 
    # result = alert(content=Change_note(item=change_copy), title="Update Change Note", buttons=[], large=True)
    # # open_form('Lists')
 
    
    

  def delete_change_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('audit_history')
    # if confirm("Are you sure you want to archive {}?".format(self.item['title'])):
    #   anvil.server.call('delete_change_note', self.item)
    #   # self.item['stage'] = 'Archive'
     # self.parent.raise_event('x-refresh-change_notes')

    pass

  # def text_box_2_pressed_enter(self, **event_args):
  #   """This method is called when the user presses Enter in this text box"""
  #   pass

  def audit_history_button_click(self, **event_args):
     result = alert(content=audit_history(self.item['new_change_note_id'], self.item['title']), title="Audit", buttons=[("Cancel", False)], large=True)

  def delete_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if confirm("Are you sure you want to archive {}?".format(self.item['title'])):
      anvil.server.call('delete_change_note', self.item)
    pass

  # def type_textbox_pressed_enter(self, **event_args):
  #   """This method is called when the user presses Enter in this text box"""
  #   pass

  # def text_box_2_pressed_enter(self, **event_args):
  #   """This method is called when the user presses Enter in this text box"""
  #   pass

  # def text_box_1_pressed_enter(self, **event_args):
  #   """This method is called when the user presses Enter in this text box"""
  #   pass

  def text_box_3_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    self.title.text = self.item['title']
    pass

 















