from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel


class TimeBankTransactionBase(BaseModel):
    value: int
    timestamp: datetime


class TimeBankTransactionCreate(TimeBankTransactionBase):
    pass


class TimeBankTransaction(TimeBankTransactionBase):
    id: int
    employee_id: int


class TimeBankBase(BaseModel):
    credit: int
    debt: int


class TimeBankCreate(TimeBankBase):
    pass


class TimeBank(TimeBankBase):
    id: int
    employee_id: int
    transactions: list[TimeBankTransaction] = []

    class Config:
        from_attributes = True


class TimeClockRecordBase(BaseModel):
    clock_in_out: datetime
    type: str


class TimeClockRecordCreate(TimeClockRecordBase):
    pass


class TimeClockRecord(TimeClockRecordBase):
    id: int
    employee_id: int
    time_clock_report_id: int

    class Config:
        from_attributes = True


class TimeClockReportApprovalBase(BaseModel):
    timestamp: datetime


class TimeClockReportApprovalCreate(TimeClockReportApprovalBase):
    pass


class TimeClockReportApproval(TimeClockReportApprovalBase):
    leader_id: int
    report_id: int

    class Config:
        from_attributes = True


class TimeClockReportSignatureBase(BaseModel):
    timestamp: datetime


class TimeClockReportSignatureCreate(TimeClockReportSignatureBase):
    pass


class TimeClockReportSignature(TimeClockReportSignatureBase):
    employee_id: int
    report_id: int

    class Config:
        from_attributes = True


class TimeClockReportBase(BaseModel):
    created_at: datetime


class TimeClockReportCreate(TimeClockReportBase):
    pass


class TimeClockReport(TimeClockReportBase):
    id: int
    employee_id: int
    configuration_id: int
    signatures: list[TimeClockReportSignature] = []
    approvals: list[TimeClockReportApproval] = []
    records: list[TimeClockRecord] = []

    class Config:
        from_attributes = True


class TimeClockConfigurationBase(BaseModel):
    name: str
    report_closing_day: int
    report_duration_days: int


class TimeClockConfigurationCreate(TimeClockConfigurationBase):
    pass


class TimeClockConfiguration(TimeClockConfigurationBase):
    id: int
    reports: list[TimeClockReport] = []

    class Config:
        from_attributes = True


class DaysOffTableBase(BaseModel):
    date: date
    type: str


class DaysOffTableCreate(DaysOffTableBase):
    pass


class DaysOffTable(DaysOffTableBase):
    id: int
    calendar_id: int

    class Config:
        from_attributes = True


class HolidayTableBase(BaseModel):
    name: str
    date: date


class HolidayTableCreate(HolidayTableBase):
    pass


class HolidayTable(HolidayTableBase):
    id: int
    calendar_id: int

    class Config:
        from_attributes = True


class CalendarBase(BaseModel):
    name: str


class CalendarCreate(CalendarBase):
    pass


class Calendar(CalendarBase):
    id: int
    work_schedule_id: int
    holiday_table: HolidayTable = None
    days_off_table: DaysOffTable = None

    class Config:
        from_attributes = True


class WorkScheduleBase(BaseModel):
    work_days: str
    work_hours: int
    start_time: int


class WorkScheduleCreate(WorkScheduleBase):
    pass


class WorkSchedule(WorkScheduleBase):
    id: int
    employee_id: int
    calendar: Calendar = None

    class Config:
        from_attributes = True


class EmployeeBase(BaseModel):
    name: str
    email: str
    leader: bool
    status: str
    team_id: int


class EmployeeCreate(EmployeeBase):
    password: str


class EmployeeUpdate(EmployeeBase):
    password: str


class Employee(EmployeeBase):
    id: int
    work_schedule: WorkSchedule = None
    time_bank: TimeBank = None
    time_bank_transactions: list[TimeBankTransaction] = []
    time_clock_report_signatures: list[TimeClockReportSignature] = []
    time_clock_report_approvals: list[TimeClockReportApproval] = []

    class Config:
        from_attributes = True


class TeamBase(BaseModel):
    name: str


class TeamCreate(TeamBase):
    pass


class TeamUpdate(TeamBase):
    pass


class Team(TeamBase):
    id: int
    members: list[Employee] = []

    class Config:
        from_attributes = True
