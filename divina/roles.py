from rolepermissions.roles import AbstractUserRole

class BasicRole(AbstractUserRole):
    role_name = 'Basic'
    available_permissions = {
        'add_content': True,
        'view_content': True,
        'edit_content': True,
    }

class FullRole(AbstractUserRole):
    role_name = 'Full'
    available_permissions = {
        'add_content': True,
        'view_content': True,
        'edit_content': True,
        'delete_content': True,
    }

class ViewOnlyRole(AbstractUserRole):
    role_name = 'ViewOnly'
    available_permissions = {
        'view_content': True,
    }