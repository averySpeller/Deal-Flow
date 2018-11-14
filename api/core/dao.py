#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Author      : Carter Bourette
# Description : ..
#               ...
#----------------------------------------------------------------------------
#
# Use explicit package path so that modules may be imported from parent.
# As per: https://docs.python.org/3/tutorial/modules.html#packages
#
from api.core.database import *

#
# TODO: Relations
# one to one.. self and other table f-key
# one to many.. use document table as f-key in model resource table
# many to one.. use resource table as f-key to document table
# many to many.. give n..m table name

class DAO:

    def __init__(self, relation=None, bulk=False):
        self._relation = relation
        self._db = DBWrapper( DBExplodeOnError() )
        self._is_bulk = bulk
        self.result_buffer = []

    def fetch_buffer(self):
        return self.result_buffer

    def create(self, relation, payload):
        def format_insert(relation, keys, values):
            query_string = 'insert into ' + relation + ' ('

            cnt = 0
            for key in keys:
                if cnt == len(keys) - 1:
                    query_string = query_string + key +') values ('
                else: query_string = query_string + key + ','
                cnt = cnt + 1

            cnt = 0
            for value in values:
                if cnt == len(keys) - 1:
                    query_string = query_string + '%s)'
                else: query_string = query_string + '%s,'
                cnt = cnt + 1

            return query_string

        if relation is None:
            relation = self._relation

        # Start a transaction
        self._db.begin_transaction()

        q = format_insert(relation, payload.keys(), payload.values())
        self._db.query(q, (*payload.values(),))
        self._db.commit()

        # Lookup the record to obtain the id
        self._db.query('select * from ' + relation +' order by ' + relation + '_id desc limit 1')

        record = self._db.fetch_one()
        self._db.end_transaction()

        return record

    def read(self, relation, id=None):
        if relation is None:
            relation = self._relation

        self._db.query('select * from ' + relation + ' where ' + relation + '_id = %s limit 1', (id))
        return self._db.fetch_one()

    def update(self, relation, id, payload):
        def format_update(relation, keys, id):
            query_string = 'update ' + relation + ' set '

            cnt = 0
            for key in keys:
                if cnt == len(keys) - 1:
                    query_string = query_string + key + ' = %s where ' + relation + '_id = ' + id
                else: query_string = query_string + key + ' = %s,'
                cnt = cnt + 1

            return query_string
        if relation is None:
            relation = self._relation

        query = format_update(relation, payload.keys(), id)

        self._db.query(query, (*payload.values(),))

    def delete(self, relation, id):
        self._db.query('delete from ' + relation + ' where ' + relation + '_id = %s', (id,))
        return self._db.cursor.rowcount > 0 and not self._db.error()

    def bulk_create(self): pass

    def bulk_read(self, relation, page_size=30, current_page=1, parser=None):
        if relation is None:
            relation = self._relation

        where_condition = ''
        if parser:
            page_size = parser.page_size
            current_page = parser.page

            print(parser.url_query)

            all_values = []
            # create the lookup filter query string
            for key,value in parser.url_query.items():

                # TODO:
                # this will allow us to fire search
                # /contacts?first:like=search_data,last:like=search_data
                # /organizations?name:like=search_data
                # Returns search results in arraylist form [ {...}, {...} ] from the resource 

                # split the key
                # parse the second key word

                # like, gt, lt, gte, lte, ne

                # END --

                # Single
                if isinstance(value, str):
                    all_values.append(value)
                    if len(all_values) > 1:
                        where_condition = where_condition + ' or ' + key + ' = %s'
                    else:
                        where_condition = where_condition + ' where ' + key + ' = %s'
                # or separated
                else:
                    for v in value:
                        all_values.append(v)
                        if len(all_values) > 1:
                            where_condition = where_condition + ' or ' + key + ' = %s'
                        else:
                            where_condition = where_condition + ' where ' + key + ' = %s'

        offset = (current_page - 1) * page_size

        try:
            self._db.query('select * from ' + relation + ' ' + where_condition + ' limit ' + str(offset) + ', ' + str(page_size), (*all_values,))
            self.result_buffer = self._db.fetch_all()
        except Exception as err:
            self.result_buffer = []
            print(err)

    def bulk_update(self): pass

    def bulk_delete(self): pass
