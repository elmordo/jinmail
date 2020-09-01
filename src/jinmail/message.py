# -*- coding: utf-8 -*-
"""
"""

__copyright__ = "Copyright (c) 2015-2020 Ing. Petr Jindra. All Rights Reserved."

from typing import List, Optional


class Address(object):

    def __init__(self, email_address: str, name: Optional[str] = None):
        self.name = name
        self.email_address = email_address

    def __str__(self):
        return self.format()

    def format(self) -> str:
        if self.name is None:
            return self.email_address
        else:
            name = self._format_name()
            return '"{name}" <{addr}>'.format(name=name, addr=self.email_address)

    def _format_name(self) -> str:
        return self.name


class Message(object):

    def __init__(self):
        self.__sender: Address = Address("")
        self.__to: List[Address] = []
        self.__cc: List[Address] = []
        self.__bcc: List[Address] = []

