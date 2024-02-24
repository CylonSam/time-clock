from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    members = relationship("Employee", back_populates="team")


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    leader = Column(Boolean)
    status = Column(String)
    team_id = Column(Integer, ForeignKey("teams.id"))

    team = relationship("Team", back_populates="members")
    work_schedule = relationship("WorkSchedule", back_populates="employee")
    time_bank = relationship("TimeBank", back_populates="employee")
    time_bank_transactions = relationship("TimeBankTransaction", back_populates="employee")
    time_clock_report = relationship("TimeClockReport", back_populates="employee")
    time_clock_records = relationship("TimeClockRecord", back_populates="employee")
    time_clock_report_signatures = relationship("TimeClockReportSignature", back_populates="employee")
    time_clock_report_approvals = relationship("TimeClockReportApproval", back_populates="leader")


class WorkSchedule(Base):
    __tablename__ = "work_schedules"

    id = Column(Integer, primary_key=True)
    work_days = Column(String)  # 0111110
    work_hours = Column(Integer)
    start_time = Column(Integer)  # Start time in minutes
    employee_id = Column(Integer, ForeignKey("employees.id"))
    calendar_id = Column(Integer, ForeignKey("calendars.id"))

    employee = relationship("Employee", back_populates="work_schedule")
    calendar = relationship("Calendar", back_populates="work_schedules")


class Calendar(Base):
    __tablename__ = "calendars"

    id = Column(Integer, primary_key=True)
    city = Column(String)
    state = Column(String)

    holiday_table = relationship("HolidayTable", back_populates="calendars")
    work_schedules = relationship("WorkSchedule", back_populates="calendar")


class HolidayTable(Base):
    __tablename__ = "holiday_table"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    date = Column(Date)
    calendar_id = Column(Integer, ForeignKey("calendars.id"))

    calendars = relationship("Calendar", back_populates="holiday_table")


class TimeClockConfiguration(Base):
    __tablename__ = "time_clock_configurations"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    report_closing_day = Column(Integer)
    report_duration_days = Column(Integer)

    reports = relationship("TimeClockReport", back_populates="configuration")


class TimeClockReport(Base):
    __tablename__ = "time_clock_reports"

    id = Column(Integer, primary_key=True)
    created_at = Column(Date)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    configuration_id = Column(Integer, ForeignKey("time_clock_configurations.id"))

    employee = relationship("Employee", back_populates="time_clock_report")
    configuration = relationship("TimeClockConfiguration", back_populates="reports")
    records = relationship("TimeClockRecord", back_populates="time_clock_report")
    signatures = relationship("TimeClockReportSignature", back_populates="report")
    approvals = relationship("TimeClockReportApproval", back_populates="report")


class TimeClockReportSignature(Base):
    __tablename__ = "time_clock_report_signatures"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    report_id = Column(Integer, ForeignKey("time_clock_reports.id"))
    timestamp = Column(DateTime)

    employee = relationship("Employee", back_populates="time_clock_report_signatures")
    report = relationship("TimeClockReport", back_populates="signatures")


class TimeClockReportApproval(Base):
    __tablename__ = "time_clock_report_approvals"

    id = Column(Integer, primary_key=True)
    leader_id = Column(Integer, ForeignKey("employees.id"))
    report_id = Column(Integer, ForeignKey("time_clock_reports.id"))
    timestamp = Column(DateTime)

    leader = relationship("Employee", back_populates="time_clock_report_approvals")
    report = relationship("TimeClockReport", back_populates="approvals")


class TimeClockRecord(Base):
    __tablename__ = "time_clock_records"

    id = Column(Integer, primary_key=True)
    clock_in_out = Column(DateTime)
    type = Column(String)  # IN or OUT
    employee_id = Column(Integer, ForeignKey("employees.id"))
    time_clock_report_id = Column(Integer, ForeignKey("time_clock_reports.id"))

    employee = relationship("Employee", back_populates="time_clock_records")
    time_clock_report = relationship("TimeClockReport", back_populates="records")


class TimeBank(Base):
    __tablename__ = "time_banks"

    id = Column(Integer, primary_key=True)
    credit = Column(Integer)
    debt = Column(Integer)
    employee_id = Column(Integer, ForeignKey("employees.id"))

    employee = relationship("Employee", back_populates="time_bank")
    transactions = relationship("TimeBankTransaction", back_populates="time_bank")


class TimeBankTransaction(Base):
    __tablename__ = "time_bank_transactions"

    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    timestamp = Column(DateTime)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    time_bank_id = Column(Integer, ForeignKey("time_banks.id"))

    employee = relationship("Employee", back_populates="time_bank_transactions")
    time_bank = relationship("TimeBank", back_populates="transactions")

    