from utils.utils import db
from datetime import datetime, date
from Models.employee_model import Employees
from Models.book_model import Books
from Models.member_model import Members

from datetime import datetime

class Transactions(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    issue_date = db.Column(db.Date, default=date.today, nullable=False)
    return_date = db.Column(db.Date)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id', onupdate="CASCADE"), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id', onupdate="CASCADE"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id', onupdate="CASCADE"), nullable=False)

    # Relationships to retrieve related data if needed
    employee = db.relationship('Employees', backref='transactions', lazy=True)
    member = db.relationship('Members', backref='transactions', lazy=True)
    book = db.relationship('Books', backref='transactions', lazy=True)

    def __repr__(self):
        return f"<Transaction {self.id} - {self.type}>"
    
    def to_dict(self):
        """Convert the TransactionModel instance into a dictionary format."""
        return {
            'id': self.id,
            'issue_date': self.issue_date if self.issue_date else None,
            'return_date': self.return_date if self.return_date else None,
            'employee_id': self.employee_id,
            'member_id': self.member_id,
            'book_id': self.book_id,
            'book_title':Books.query.filter_by(id = self.book_id).first().title,
            'author_name':Books.query.filter_by(id = self.book_id).first().to_dict()["author"],
            'employee': self.employee.to_dict() if self.employee else None,
            'member': self.member.to_dict() if self.member else None,
            'book': self.book.to_dict() if self.book else None
        }