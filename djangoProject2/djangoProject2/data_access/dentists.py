from djangoProject2.data_access.setup_database import get_engine
from sqlalchemy import text


def getDentistsFromDatabase(branch_id: str):
    query = text("SELECT employee_id , d.branch_id FROM branch b "
                 "inner join dentist on d.branch_id = b.branch_id"
                 "where d.branch_id = :branch_id")
    with get_engine().connect() as conn:
        data = conn.execute(query, branch_id=branch_id)
    return data.mappings.all()
