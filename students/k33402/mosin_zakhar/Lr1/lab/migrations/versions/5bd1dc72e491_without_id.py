"""without id

Revision ID: 5bd1dc72e491
Revises: 61f8fd55f8de
Create Date: 2024-08-19 17:34:48.597392

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '5bd1dc72e491'
down_revision: Union[str, None] = '61f8fd55f8de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('wishlist', 'id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wishlist', sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
