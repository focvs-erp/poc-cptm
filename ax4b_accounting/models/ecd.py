from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError, Warning
from openerp.tools import config


class Ecd(models.Model):
    _name = 'account.ecd'
    _description = 'ECD'
    
    name = fields.Char(string="Gerar ECD") 
    org_fis = fields.Char(string="Organização Fiscal")
    tp_res = fields.Char(string="Tipo de Reserva")
    de = fields.Date(string="De")
    ate = fields.Date(string="Áte")
    inc_dem = fields.Boolean(string="Incluir Demonstrativel Contaveis")
    periodo = fields.Selection([('0', 'Mensal'), ('1', 'Anual')])
    sit_emp = fields.Selection([('0', 'Divisão'), ('1', 'Fusão'), ('2', 'Corporação'), ('3', 'Fechamento'), ('4', 'Transformação')], string="Situação da Empresa")
    per_abe = fields.Selection([('0', 'Normal'), ('1', 'Abertura'), ('2', 'Divisão,Fusão ou Aquisição')], string="Período Fiscal de Abertura")
    versao = fields.Selection([('0', '2.00'), ('1', '3.00'),  ('2', '4.00'),  ('3', '5.00'),  ('4', '6.00'),  ('5', '7.00')], string="Versão do Layout")
    tp_arq = fields.Selection([('0', 'Oríginal'), ('1', 'Substítuto')], string="Tipo de Arquivo")
    dt_enc = fields.Date(string="Data de Encerramento Exercicio Social")
    tp_inst = fields.Selection([('0', 'Pj em Geral'), ('1', 'Pj em Geral-Lucro Presumido'),  ('2', 'Financeiras'),  ('3','Seguradoras'),  ('4', 'Imunes e Insentas em Geral'),  ('5', 'Imunes e Insentas-Financeiras'),  ('6', 'Imunes e Insentas-Seguradoras'),  ('7', 'Entidade Fechadas de Previdencias Complementar'), ('8', 'Partídos Políticos'), ('9', 'Lucro Presumidos-Financeiras')], string="Tipo de Instituição" )
    num_Livro = fields.Char(string="Número do Livro")
    
    def btn_ok(self):
    
        message_id = self.env['account.message'].create({'message': 'Os arquivos foram gerados com Sucesso!'})
        return {
            'name': 'Message',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'account.message',
            'res_id': message_id.id,
            'target': 'new'
        }
 
   

class EdcMessage(models.TransientModel):
    _name = 'account.message'
    _description = "Show Message"

    message = fields.Text('Message', required=True)

    def action_close(self):
        return {'type': 'ir.actions.act_window_close'}

    