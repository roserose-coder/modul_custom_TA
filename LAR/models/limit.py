from odoo import models, fields, api


class limit_invoice(models.Model):
    _name = 'limit.invoice'
    _inherit = ['mail.thread']

    priority = fields.Integer("Priority")

    currency_id = fields.Many2one('res.currency', domain=[('name', 'in', ('IDR', 'USD'))],
                                  default=lambda self: self.env.user.company_id.currency_id.id,readonly=True)
    value = fields.Monetary("Value", tracking=True, currency_field='currency_id')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id)
    active = fields.Boolean("Active", default=True)
    partner_id = fields.Many2one('res.partner')
    credit_amount = fields.Monetary("Credit Amount", tracking=True, currency_field='currency_id')


class partner_credit(models.Model):
    _inherit = ['account.move']

    @api.model
    def action_post(self):
        print('test-------------------')
        # print(self.env['account.move'].search(['id','=',self.id]))
        # account = self.env['account.move'].browse(self.id)

        account = self.env['account.move'].search([('id', '=', self.id)])

        limit = self.env['limit.invoice'].search(
            [['partner_id', '=', account.partner_id.id], ['company_id', '=', self.env.user.company_id.id]])

        if limit:
            jumlah_uang = account.amount_total
            batas_credit = limit.value
            kredit_saat_ini = limit.credit_amount

            if batas_credit < kredit_saat_ini + jumlah_uang:
                raise models.ValidationError('This customer has reached their credit limit')

            kredit_saat_ini += jumlah_uang
            limit.write({'credit_amount': kredit_saat_ini})

        return super(partner_credit, self).action_post()

        # print(self.env['account.move'].browse(self.id))
        # test = super(partner_credit, self).action_post()
        # # print(test)
        # return test

    def button_draft(self):

        account = self.env['account.move'].search([('id', '=', self.id)])
        limit = self.env['limit.invoice'].search(
            [['partner_id', '=', account.partner_id.id], ['company_id', '=', self.env.user.company_id.id]])

        if limit:
            jumlah_uang = account.amount_total
            kredit_saat_ini = limit.credit_amount

            kredit_saat_ini -= jumlah_uang
            limit.write({'credit_amount': kredit_saat_ini})
        return super(partner_credit, self).button_draft()


    # @api.model
    # def create(self, vals):
    #     print('test-------------------')
    #     print(vals)
    #     # self.env['res.partner'].search([['is_company', '=', True], ['customer', '=', True]])
    #     test = self.env['limit.invoice'].search(
    #         [['partner_id', '=', vals.get('partner_id')], ['company_id', '=', self.env.user.company_id.id]])
    #     print(test.credit_amount, '----', test.partner_id.name)
    #
    #     return super(partner_credit, self).create(vals)


class partner_payment(models.TransientModel):
    _inherit = ['account.payment.register']

    def action_create_payments(self):
        print('oke test')

        data_invoices = self.env['account.move'].browse(self._context.get('active_ids', []))
        for data_invoice in data_invoices:
            limit = self.env['limit.invoice'].search(
                [['partner_id', '=', data_invoice.partner_id.id], ['company_id', '=', self.env.user.company_id.id]])
            if limit:
                # jumlah_uang = data_invoice.amount_total

                for data in self:
                    jumlah_uang = data.amount
                # batas_kredit = data_invoice.value
                kredit_saat_ini = limit.credit_amount

                kredit_saat_ini -= jumlah_uang

                limit.write({'credit_amount': kredit_saat_ini})
        return super(partner_payment, self).action_create_payments()


class partner_payment_reversal(models.TransientModel):
    _inherit = ['account.move.reversal']

    def reverse_moves(self):
        self.ensure_one()

        moves = self.move_ids
        for move in moves:

            partner_id = move.partner_id.id
            jumlah_uang = move.amount_total
            limit = self.env['limit.invoice'].search(
                [['partner_id', '=', partner_id], ['company_id', '=', self.env.user.company_id.id]])
            if limit:
                kredit_saat_ini = limit.credit_amount
                if self.refund_method =='refund':
                    jumlah_uang/=2

                kredit_saat_ini-= jumlah_uang
                limit.write({'credit_amount': kredit_saat_ini})

                # for data in self:
                #    if  data.refund_method == 'refund':
                #
                #    elif data.refund_method=='cancel':
        return super(partner_payment_reversal,self).reverse_moves()