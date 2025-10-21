class Calc():
    """Calculator class–acts like an old school printing calculator."""
    def __init__(self):
        """Same as ac()--see below"""
        self.ac()

    
    def __repr__(self):
        """The string representation of Calc() is the list of calculations."""
        return self.showcalc()

        
    def __add__(self, other):
        """Combine the totals and the lists of caclulations."""
        self.calculations.extend(other.calculations)
        self.total = other.total
        return self

    
    def determine_values(self, op1, op2):
        """Determine what first and second operand are."""
        if op2 is None:
            return self.total, op1
        return op1, op2

    
    def notecalc(self, op, op1, op2=None):
        """Add latest calculation to the running list."""
        calc = ''
        if op == 'log':
            op += op2
        else:
            calc = str(op1) + " "
        calc += str(op) + ' ' + str(op2) + ' = ' + str(self.total)
        self.calculations.append(calc)


    def perform_operation(self, oper, op1, op2):
        """Figure out op1 and op2 and note the calculation being performed."""
        import operator
        
        calc_mapper = { # could put this elsewhere
             '+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv,
            '**': operator.pow,
        }
        
        op1, op2 = self.determine_values(op1, op2)
        self.total = calc_mapper[oper](op1, op2)
        self.notecalc(oper, op1, op2)

        return op1, op2

                          
    def add(self, op1, op2=None):
        """Add two numbers. If only one number supplied, add to running total."""
        op1, op2 = self.perform_operation('+', op1, op2)
        return self.total

    
    def sub(self, op1, op2=None):
        """Subtract two numbers or subtract from running total."""
        op1, op2 = self.perform_operation('-', op1, op2)
        return self.total

    
    def mul(self, op1, op2=None):
        """Multiply two numbers or multiply by running total."""
        op1, op2 = self.perform_operation('*', op1, op2)
        return self.total

    
    def pow(self, op1, op2=None):
        """Raise a number to a power, or raise the running total to the power"""
        op1, op2 = self.perform_operation('**', op1, op2)
        return self.total

    
    def showcalc(self):
        """Show current list of calculations."""
        return '\n'.join(self.calculations)

    
    def ac(self):
        """Set total to 0 and erase the list of calculations ("All clear")."""
        self.calculations = []
        self.total = 0