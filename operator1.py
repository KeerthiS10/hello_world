def test_cycle_downstream_loop(self):
        # test downstream self loop
        dag = DAG(
            'dag',
            start_date=DEFAULT_DATE,
            default_args={'owner': 'keerthi'})

        # A -> B -> C -> D -> E -> E
        with dag:
            op1 = DummyOperator(task_id='A')
            op2 = DummyOperator(task_id='B')
            op3 = DummyOperator(task_id='C')
            op4 = DummyOperator(task_id='D')
            op5 = DummyOperator(task_id='E')
            op1.set_downstream(op2)
            op2.set_downstream(op3)
            op3.set_downstream(op4)
            op4.set_downstream(op5)
            op5.set_downstream(op5)

        with self.assertRaises(AirflowDagCycleException):
            self.assertFalse(test_cycle(dag)) 
