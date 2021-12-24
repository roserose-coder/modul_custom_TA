# -*- coding: utf-8 -*-
from odoo import models, api, fields, tools


class RoomRentingStatistics(models.Model):
    _name = 'room.renting.statistics'
    _auto = False

    room_id = fields.Many2one('roomster.room', 'Room', readonly=True)
    rent_count = fields.Integer(string="Times booked", readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        query = """
        CREATE OR REPLACE VIEW room_renting_statistics AS (
          SELECT
                min(rb.id) as id,
                rb.name as room_id,
                count(rb.id) as rent_count
               

            FROM
                roomster_booked AS rb
            JOIN
                roomster_room as rr ON rr.id = rb.name
	        group by
	            room_id
        );
        """
        self.env.cr.execute(query)
