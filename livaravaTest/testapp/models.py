#!/usr/bin/env python
# -*- coding: utf-8 -*-
from neomodel import (StructuredNode, StringProperty,
                      IntegerProperty, ArrayProperty,
                      RelationshipTo, RelationshipFrom)


class Author(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    verse = RelationshipFrom('Verse', 'WRITTEN_BY')


class Verse(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    text = StringProperty(required=True)
    author = RelationshipTo('Author', 'WRITTEN_BY')
    year = RelationshipTo('Year', 'WRITTEN_DURING')
    reviews = ArrayProperty()
    likes = IntegerProperty(default=0)


class Year(StructuredNode):
    year = IntegerProperty(unique_index=True, required=True)
    verse = RelationshipFrom('Verse', 'WRITTEN_DURING')
