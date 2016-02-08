##Simple version of Trello Web Application

###Requirements
1. Allow edit/create/delete Status entity in the admin page
  * Status has only one field - name
  * Name value could be only one of (New/InProgress/OnReview/Tested/Delivered)
  * Names should be unique. If user try's to create Status that already exists he should get an error - RUS "Данный статус уже существует" (ENG - "This status already exists")

2. In Admin page you can edit/create/delete Task entity
  * Task has field name, which can not be empty
  * Task has field status, which can be only one of the existing statuses

3. Applications should display Statuses with corresponding tasks 
  * All statuses and tasks should be displayed on one page

4. Application should allow to change tasks statuses by drag-and-drop
  * Changes on DOM should not reload the whole page, only specific elements 

Application should be developed on Python 2.7 using Django framework. No restrictions on front-end frameworks.
