If new files is been added, first run:

```bash
invenio-cli assets build
```
then update change on save with:
```bash
invenio-cli assets watch
```

weird error
```console
[2022-11-29 17:26:49,368] WARNING in views: Pages were not loaded.
127.0.0.1 - - [29/Nov/2022 17:26:49] "GET / HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1900, in _execute_context
    self.dialect.do_execute(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 736, in do_execute
    cursor.execute(statement, parameters)
psycopg2.errors.UndefinedTable: relation "pages_page" does not exist
LINE 2: FROM pages_page
             ^


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/flask/app.py", line 2548, in __call__
    return self.wsgi_app(environ, start_response)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/werkzeug/middleware/proxy_fix.py", line 187, in __call__
    return self.app(environ, start_response)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/werkzeug/middleware/dispatcher.py", line 78, in __call__
    return app(environ, start_response)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/flask/app.py", line 2528, in wsgi_app
    response = self.handle_exception(e)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/flask/app.py", line 2525, in wsgi_app
    response = self.full_dispatch_request()
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/flask/app.py", line 1812, in full_dispatch_request
    self.ensure_sync(func)()
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/invenio_pages/views.py", line 49, in preload_pages
    _add_url_rule([page.url for page in Page.query.all()])
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/orm/query.py", line 2772, in all
    return self._iter().all()
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/orm/query.py", line 2915, in _iter
    result = self.session.execute(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/orm/session.py", line 1714, in execute
    result = conn._execute_20(statement, params or {}, execution_options)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1705, in _execute_20
    return meth(self, args_10style, kwargs_10style, execution_options)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/sql/elements.py", line 334, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1572, in _execute_clauseelement
    ret = self._execute_context(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1943, in _execute_context
    self._handle_dbapi_exception(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 2124, in _handle_dbapi_exception
    util.raise_(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/util/compat.py", line 210, in raise_
    raise exception
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1900, in _execute_context
    self.dialect.do_execute(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 736, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) relation "pages_page" does not exist
LINE 2: FROM pages_page
             ^

[SQL: SELECT pages_page.created AS pages_page_created, pages_page.updated AS pages_page_updated, pages_page.id AS pages_page_id, pages_page.url AS pages_page_url, pages_page.title AS pages_page_title, pages_page.content AS pages_page_content, pages_page.description AS pages_page_description, pages_page.template_name AS pages_page_template_name
FROM pages_page]
(Background on this error at: https://sqlalche.me/e/14/f405)
127.0.0.1 - - [29/Nov/2022 17:26:49] "GET /?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 200 -
127.0.0.1 - - [29/Nov/2022 17:26:49] "GET /?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 200 -
127.0.0.1 - - [29/Nov/2022 17:26:49] "GET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 200 -
127.0.0.1 - - [29/Nov/2022 17:26:49] "GET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 200 -
[2022-11-29 17:26:53,031: INFO/Beat] Scheduler: Sending due task indexer (invenio_records_resources.tasks.manage_indexer_queues)
[2022-11-29 17:26:53,033: INFO/MainProcess] Task invenio_records_resources.tasks.manage_indexer_queues[ba3f0b6d-1cdf-4912-a98a-4414397e7513] received
[2022-11-29 17:26:53,051: INFO/ForkPoolWorker-9] Task invenio_records_resources.tasks.manage_indexer_queues[ba3f0b6d-1cdf-4912-a98a-4414397e7513] succeeded in 0.016869045997736976s: None
[2022-11-29 17:27:03,031: INFO/Beat] Scheduler: Sending due task indexer (invenio_records_resources.tasks.manage_indexer_queues)
[2022-11-29 17:27:03,033: INFO/MainProcess] Task invenio_records_resources.tasks.manage_indexer_queues[52a03528-9009-4606-86ea-8fd39a3e5a3b] received
[2022-11-29 17:27:03,050: INFO/ForkPoolWorker-9] Task invenio_records_resources.tasks.manage_indexer_queues[52a03528-9009-4606-86ea-8fd39a3e5a3b] succeeded in 0.01617961000010837s: None
127.0.0.1 - - [29/Nov/2022 17:27:11] "GET / HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/flask/app.py", line 2548, in __call__
    return self.wsgi_app(environ, start_response)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/werkzeug/middleware/proxy_fix.py", line 187, in __call__
    return self.app(environ, start_response)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/werkzeug/middleware/dispatcher.py", line 78, in __call__
    return app(environ, start_response)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/flask/app.py", line 2528, in wsgi_app
    response = self.handle_exception(e)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/flask/app.py", line 2525, in wsgi_app
    response = self.full_dispatch_request()
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/flask/app.py", line 1812, in full_dispatch_request
    self.ensure_sync(func)()
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/invenio_administration/admin.py", line 67, in init_menu
    self._menu.register_menu_entries(current_menu, self._menu_key)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/invenio_administration/menu/menu.py", line 63, in register_menu_entries
    main_menu.submenu(name).register(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/flask_menu/__init__.py", line 145, in register
    raise RuntimeError('Can not override existing attribute '
RuntimeError: Can not override existing attribute icon.
127.0.0.1 - - [29/Nov/2022 17:27:11] "GET /?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 200 -


[2022-11-29 17:28:09,298: INFO/Beat] Scheduler: Sending due task draft_resources (invenio_drafts_resources.services.records.tasks.cleanup_drafts)
[2022-11-29 17:28:09,300: INFO/MainProcess] Task invenio_drafts_resources.services.records.tasks.cleanup_drafts[b1f0befb-ed9d-4c45-bc3b-46f4d19af38b] received
[2022-11-29 17:28:09,324: ERROR/ForkPoolWorker-9] Task invenio_drafts_resources.services.records.tasks.cleanup_drafts[b1f0befb-ed9d-4c45-bc3b-46f4d19af38b] raised unexpected: ProgrammingError('(psycopg2.errors.UndefinedTable) relation "rdm_drafts_metadata" does not exist\nLINE 2: FROM rdm_drafts_metadata \n             ^\n')
Traceback (most recent call last):
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1900, in _execute_context
    self.dialect.do_execute(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 736, in do_execute
    cursor.execute(statement, parameters)
psycopg2.errors.UndefinedTable: relation "rdm_drafts_metadata" does not exist
LINE 2: FROM rdm_drafts_metadata
             ^


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/celery/app/trace.py", line 451, in trace_task
    R = retval = fun(*args, **kwargs)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/flask_celeryext/app.py", line 71, in __call__
    return Task.__call__(self, *args, **kwargs)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/celery/app/trace.py", line 734, in __protected_call__
    return self.run(*args, **kwargs)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/invenio_drafts_resources/services/records/tasks.py", line 26, in cleanup_drafts
    service.cleanup_drafts(timedelta_param)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/invenio_records_resources/services/uow.py", line 324, in inner
    res = f(self, *args, **kwargs)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/invenio_drafts_resources/services/records/service.py", line 603, in cleanup_drafts
    self.draft_cls.cleanup_drafts(timedelta)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/invenio_drafts_resources/records/api.py", line 243, in cleanup_drafts
    models = draft_model.query.filter(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/orm/query.py", line 2772, in all
    return self._iter().all()
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/orm/query.py", line 2915, in _iter
    result = self.session.execute(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/orm/session.py", line 1714, in execute
    result = conn._execute_20(statement, params or {}, execution_options)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1705, in _execute_20
    return meth(self, args_10style, kwargs_10style, execution_options)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/sql/elements.py", line 334, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1572, in _execute_clauseelement
    ret = self._execute_context(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1943, in _execute_context
    self._handle_dbapi_exception(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 2124, in _handle_dbapi_exception
    util.raise_(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/util/compat.py", line 210, in raise_
    raise exception
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1900, in _execute_context
    self.dialect.do_execute(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 736, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) relation "rdm_drafts_metadata" does not exist
LINE 2: FROM rdm_drafts_metadata
             ^

[SQL: SELECT rdm_drafts_metadata.created AS rdm_drafts_metadata_created, rdm_drafts_metadata.updated AS rdm_drafts_metadata_updated, rdm_drafts_metadata.id AS rdm_drafts_metadata_id, rdm_drafts_metadata.json AS rdm_drafts_metadata_json, rdm_drafts_metadata.version_id AS rdm_drafts_metadata_version_id, rdm_drafts_metadata.index AS rdm_drafts_metadata_index, rdm_drafts_metadata.fork_version_id AS rdm_drafts_metadata_fork_version_id, rdm_drafts_metadata.expires_at AS rdm_drafts_metadata_expires_at, rdm_drafts_metadata.bucket_id AS rdm_drafts_metadata_bucket_id, rdm_drafts_metadata.parent_id AS rdm_drafts_metadata_parent_id
FROM rdm_drafts_metadata
WHERE (rdm_drafts_metadata.json IS NULL) = true AND rdm_drafts_metadata.updated < %(updated_1)s]
[parameters: {'updated_1': datetime.datetime(2022, 11, 29, 15, 28, 9, 301801)}]
(Background on this error at: https://sqlalche.me/e/14/f405)
[2022-11-29 17:28:09,328: INFO/Beat] Scheduler: Sending due task accounts_sessions (invenio_accounts.tasks.clean_session_table)
[2022-11-29 17:28:09,329: INFO/MainProcess] Task invenio_accounts.tasks.clean_session_table[b0db3371-2533-4937-8273-a462c269890c] received
[2022-11-29 17:28:09,337: ERROR/ForkPoolWorker-9] Task invenio_accounts.tasks.clean_session_table[b0db3371-2533-4937-8273-a462c269890c] raised unexpected: ProgrammingError('(psycopg2.errors.UndefinedTable) relation "accounts_user_session_activity" does not exist\nLINE 2: FROM accounts_user_session_activity \n             ^\n')
Traceback (most recent call last):
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1900, in _execute_context
    self.dialect.do_execute(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 736, in do_execute
    cursor.execute(statement, parameters)
psycopg2.errors.UndefinedTable: relation "accounts_user_session_activity" does not exist
LINE 2: FROM accounts_user_session_activity
             ^

-----


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/celery/app/trace.py", line 451, in trace_task
    R = retval = fun(*args, **kwargs)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/flask_celeryext/app.py", line 71, in __call__
    return Task.__call__(self, *args, **kwargs)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/celery/app/trace.py", line 734, in __protected_call__
    return self.run(*args, **kwargs)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/invenio_accounts/tasks.py", line 54, in clean_session_table
    sessions = SessionActivity.query_by_expired().all()
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/orm/query.py", line 2772, in all
    return self._iter().all()
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/orm/query.py", line 2915, in _iter
    result = self.session.execute(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/orm/session.py", line 1714, in execute
    result = conn._execute_20(statement, params or {}, execution_options)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1705, in _execute_20
    return meth(self, args_10style, kwargs_10style, execution_options)
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/sql/elements.py", line 334, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1572, in _execute_clauseelement
    ret = self._execute_context(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1943, in _execute_context
    self._handle_dbapi_exception(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 2124, in _handle_dbapi_exception
    util.raise_(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/util/compat.py", line 210, in raise_
    raise exception
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1900, in _execute_context
    self.dialect.do_execute(
  File "/home/samk13/.pyenv/versions/3.9.15/envs/theme-test-2-venv/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 736, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) relation "accounts_user_session_activity" does not exist
LINE 2: FROM accounts_user_session_activity
             ^

[SQL: SELECT accounts_user_session_activity.created AS accounts_user_session_activity_created, accounts_user_session_activity.updated AS accounts_user_session_activity_updated, accounts_user_session_activity.sid_s AS accounts_user_session_activity_sid_s, accounts_user_session_activity.user_id AS accounts_user_session_activity_user_id, accounts_user_session_activity.ip AS accounts_user_session_activity_ip, accounts_user_session_activity.country AS accounts_user_session_activity_country, accounts_user_session_activity.browser AS accounts_user_session_activity_browser, accounts_user_session_activity.browser_version AS accounts_user_session_activity_browser_version, accounts_user_session_activity.os AS accounts_user_session_activity_os, accounts_user_session_activity.device AS accounts_user_session_activity_device
FROM accounts_user_session_activity
WHERE accounts_user_session_activity.created < %(created_1)s]
[parameters: {'created_1': datetime.datetime(2022, 10, 29, 16, 28, 9, 330559)}]
(Background on this error at: https://sqlalche.me/e/14/f405)
```