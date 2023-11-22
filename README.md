The Cmd class provides a simple framework for writing line-oriented command interpreters. These are often useful for test harnesses, administrative tools, and prototypes that will later be wrapped in a more sophisticated interface.

class cmd.Cmd(completekey='tab', stdin=None, stdout=None)
A Cmd instance or subclass instance is a line-oriented interpreter framework. There is no good reason to instantiate Cmd itself; rather, it’s useful as a superclass of an interpreter class you define yourself in order to inherit Cmd’s methods and encapsulate action methods.

The optional argument completekey is the readline name of a completion key; it defaults to Tab. If completekey is not None and readline is available, command completion is done automatically.

The optional arguments stdin and stdout specify the input and output file objects that the Cmd instance or subclass instance will use for input and output. If not specified, they will default to sys.stdin and sys.stdout.

If you want a given stdin to be used, make sure to set the instance’s use_rawinput attribute to False, otherwise stdin will be ignored.
QLAlchemy Core
The breadth of SQLAlchemy’s SQL rendering engine, DBAPI integration, transaction integration, and schema description services are documented here. In contrast to the ORM’s domain-centric mode of usage, the SQL Expression Language provides a schema-centric usage paradigm.

Read this first: SQL Expression Language Tutorial

All the Built In SQL: SQL Expression API

Engines, Connections, Pools: Engine Configuration | Connections, Transactions | Connection Pooling

Schema Definition: Overview | Tables and Columns | Database Introspection (Reflection) | Insert/Update Defaults | Constraints and Indexes | Using Data Definition Language (DDL)

Datatypes: Overview | Building Custom Types | API

Core Basics: Overview | Runtime Inspection API | Event System | Core Event Interfaces | Creating Custom SQL Constructs |

Dialect Documentation
13.1.2 ALTER DATABASE Statement
ALTER {DATABASE | SCHEMA} [db_name]
    alter_option ...

alter_option: {
    [DEFAULT] CHARACTER SET [=] charset_name
  | [DEFAULT] COLLATE [=] collation_name
  | [DEFAULT] ENCRYPTION [=] {'Y' | 'N'}
  | READ ONLY [=] {DEFAULT | 0 | 1}
}
ALTER DATABASE enables you to change the overall characteristics of a database. These characteristics are stored in the data dictionary. This statement requires the ALTER privilege on the database. ALTER SCHEMA is a synonym for ALTER DATABASE.

If the database name is omitted, the statement applies to the default database. In that case, an error occurs if there is no default database.

For any alter_option omitted from the statement, the database retains its current option value, with the exception that changing the character set may change the collation and vice versa.

Character Set and Collation Options

Encryption Option

Read Only Option

Character Set and Collation Options
The CHARACTER SET option changes the default database character set. The COLLATE option changes the default database collation. For information about character set and collation names, see Chapter 10, Character Sets, Collations, Unicode.

To see the available character sets and collations, use the SHOW CHARACTER SET and SHOW COLLATION statements, respectively. See Section 13.7.7.3, “SHOW CHARACTER SET Statement”, and Section 13.7.7.4, “SHOW COLLATION Statement”.

A stored routine that uses the database defaults when the routine is created includes those defaults as part of its definition. (In a stored routine, variables with character data types use the database defaults if the character set or collation are not specified explicitly. See Section 13.1.17, “CREATE PROCEDURE and CREATE FUNCTION Statements”.) If you change the default character set or collation for a database, any stored routines that are to use the new defaults must be dropped and recreated.

Encryption Option
The ENCRYPTION option, introduced in MySQL 8.0.16, defines the default database encryption, which is inherited by tables created in the database. The permitted values are 'Y' (encryption enabled) and 'N' (encryption disabled).

The mysql system schema cannot be set to default encryption. The existing tables within it are part of the general mysql tablespace, which may be encrypted. The information_schema contains only views. It is not possible to create any tables within it. There is nothing on the disk to encrypt. All tables in the performance_schema use the PERFORMANCE_SCHEMA engine, which is purely in-memory. It is not possible to create any other tables in it. There is nothing on the disk to encrypt.

Only newly created tables inherit the default database encryption. For existing tables associated with the database, their encryption remains unchanged. If the table_encryption_privilege_check system variable is enabled, the TABLE_ENCRYPTION_ADMIN privilege is required to specify a default encryption setting that differs from the value of the default_table_encryption system variable. For more information, see Defining an Encryption Default for Schemas and General Tablespaces.

Read Only Option
The READ ONLY option, introduced in MySQL 8.0.22, controls whether to permit modification of the database and objects within it. The permitted values are DEFAULT or 0 (not read only) and 1 (read only). This option is useful for database migration because a database for which READ ONLY is enabled can be migrated to another MySQL instance without concern that the database might be changed during the operation.

With NDB Cluster, making a database read only on one mysqld server is synchronized to other mysqld servers in the same cluster, so that the database becomes read only on all mysqld servers.

The READ ONLY option, if enabled, is displayed in the INFORMATION_SCHEMA SCHEMATA_EXTENSIONS table. See Section 26.3.32, “The INFORMATION_SCHEMA SCHEMATA_EXTENSIONS Table”.

The READ ONLY option cannot be enabled for these system schemas: mysql, information_schema, performance_schema.

In ALTER DATABASE statements, the READ ONLY option interacts with other instances of itself and with other options as follows:

An error occurs if multiple instances of READ ONLY conflict (for example, READ ONLY = 1 READ ONLY = 0).

An ALTER DATABASE statement that contains only (nonconflicting) READ ONLY options is permitted even for a read-only database.

A mix of (nonconflicting) READ ONLY options with other options is permitted if the read-only state of the database either before or after the statement permits modifications. If the read-only state both before and after prohibits changes, an error occurs.

This statement succeeds whether or not the database is read only:

ALTER DATABASE mydb READ ONLY = 0 DEFAULT COLLATE utf8mb4_bin;
This statement succeeds if the database is not read only, but fails if it is already read only:

ALTE
