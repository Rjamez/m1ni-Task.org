from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'your_revision_id'
down_revision = 'previous_revision_id'
branch_labels = None
depends_on = None

def upgrade():
    # Create Categories table
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.String),
    )

    # Create Task History table
    op.create_table(
        'task_history',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('task_id', sa.Integer, sa.ForeignKey('tasks.id'), nullable=False),
        sa.Column('updated_at', sa.DateTime, default=sa.func.now()),
        sa.Column('old_status', sa.String),
        sa.Column('new_status', sa.String),
        sa.Column('old_priority', sa.String),
        sa.Column('new_priority', sa.String),
    )

    # Create Task Reminders table
    op.create_table(
        'task_reminders',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('task_id', sa.Integer, sa.ForeignKey('tasks.id'), nullable=False),
        sa.Column('reminder_date', sa.DateTime, nullable=False),
    )

    # Add category_id to Tasks table
    op.add_column('tasks', sa.Column('category_id', sa.Integer, sa.ForeignKey('categories.id'), nullable=False))

def downgrade():
    # Drop the new tables and column in reverse order
    op.drop_column('tasks', 'category_id')
    op.drop_table('task_reminders')
    op.drop_table('task_history')
    op.drop_table('categories')