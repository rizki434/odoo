from odoo import models,fields
class Biodata(models.Model):
    _name = 'latihan.biodata'
    _description = 'Latihan Biodata'
    
    name = fields.Char(string='Nama')
    fullname = fields.Char(string='Nama Lengkap')
    tanggal_lahir = fields.Date(string='Tanggal Lahir')
    umur = fields.Integer(string='Umur')
    anak = fields.Integer(string='Anak')
    foto = fields.Binary(string='Foto')
    jenis_kelamin = fields.Selection([('male', 'Laki-Laki'), ('female', 'Perempuan')], string='Jenis Kelamin')
    
    pendidikan_sd = fields.Boolean(string='SD')
    pendidikan_smp = fields.Boolean(string='SMP')
    pendidikan_sltp = fields.Boolean(string='SLTP')
    pendidikan_sma = fields.Boolean(string='SMA')
    pendidikan_smk = fields.Boolean(string='SMK')
    pendidikan_smu = fields.Boolean(string='SMU')
    pendidikan_slta = fields.Boolean(string='SLTA')
    pendidikan_kuliah = fields.Boolean(string='Kuliah')
