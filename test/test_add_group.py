# -*- coding: utf-8 -*-
from model.group import Group
import pytest

def test_add_group(app, db, json_groups):
    group = json_groups
    with pytest.allure.step('Take existing group list from db'):
        old_groups = db.get_group_list()
    with pytest.allure.step('Create new group'):
        app.group.create(group)
    with pytest.allure.step('Take existing group list from db where we add groups'):
        new_groups = db.get_group_list()
    old_groups.append(group)
    with pytest.allure.step('Compare groups lists'):
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
