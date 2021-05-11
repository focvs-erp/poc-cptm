from odoo import models, fields, api

class PlanoReferencial(models.Model):
   _name = 'accounting.plano_referencial'
   _description = 'Plano Referencial'

#    prioridade = fields.Selection([('0', 'Normal'), ('1', 'Urgent')], 'Priority', default='0', index=True)
   codigo = fields.Char(string='Código')
   nome_cta = fields.Char(string='Nome da Conta')
   tipo = fields.Char(string='Tipo')
   data_ini = fields.Date(string='Data de Inicio')
   data_fin = fields.Date(string='Data Final')
   cod_ctasup = fields.Char(string='Conta Superior')
   nivel = fields.Char(string='Nível')
   natureza = fields.Char(string='Natureza')