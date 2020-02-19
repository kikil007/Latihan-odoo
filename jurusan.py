from odoo import api, fields, models

class jurusan(models.Model):
    _name   = "academic.jurusan"

    name    = fields.Char("name")
    description = fields.Text("Description")
    responsible_id  = fields.Many2one (
                                        comodel_name="res.users", #res user adalah tabel base dari odoo
                                        string= "Responsible")

