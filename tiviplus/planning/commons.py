

class MaterialLoanEditMixin(object):
	
	@static_method
	def perform_delete(user, loan):
		permission_granted = False
		if user == loan.borrower or permission_granted:
			loan.aborted = True
