Configuration
=======================
QU4RTET AS2 Gateway is configured using the Gateway's User Interface (UI). In order to access the Gateway's UI, you must have credentials.
Please ask your QU4RTET AS2 Gateway Administrator to provide you with a ``username`` and ``password``.

QU4RTET AS2 Gateway uses ``pyAS2`` to securely send AS2 Messages. ``pyAS2`` has configuration values that can be overriden.
The configuration values are listed below. The ``PYAS2`` object below should be added to QU4RTET AS2 Gateway's settings file.
However, check with a Vantage Resource before making any changes to these values.

.. code-block:: python

    PYAS2 = {
        'ENVIRONMENT' : 'production', 
        'PORT' : 8888, 
        'SSLCERTIFICATE' : '/path_to_cert/server_cert.pem', 
        'SSLPRIVATEKEY' : '/path_to_cert/server_privkey.pem',
        'DATADIR' : '/path_to_datadir/data', 
        'PYTHONPATH' : '/path_to_python/python', 
        'ENVIRONMENTTEXT' : 'BETA',  
        'ENVIRONMENTTEXTCOLOR' : 'Yellow', 
        'LOGLEVEL' : 'DEBUG', 
        'LOGCONSOLE' : True, 
        'LOGCONSOLELEVEL' : 'DEBUG', 
        'MAXRETRIES': 5,    
        'MDNURL' : 'https://192.168.1.115:8888/pyas2/as2receive', 
        'ASYNCMDNWAIT' : 30,
        'MAXARCHDAYS' : 30, 
    }

The available settings along with their usage is described below:

+------------------------+----------------------------+------------------------------------------------+
| Settings Name          | Default Value              | Usage                                          |
+========================+============================+================================================+
| ENVIRONMENT            | production                 | The as2 server in development or production    |
+------------------------+----------------------------+------------------------------------------------+
| PORT                   | 8080                       | HTTP Port as2 server listens on                |
+------------------------+----------------------------+------------------------------------------------+
| SSLCERTIFICATE         | ``None``                   | Path to the SSL Public Key                     |
+------------------------+----------------------------+------------------------------------------------+
| SSLPRIVATEKEY          | ``None``                   | Path to the SSL Private Key                    |
+------------------------+----------------------------+------------------------------------------------+
| DATADIR                | ``Django Project Path``    | Full path to the base directory for storing    | 
|                        |                            | messages, MDNs, certificates and logs          |
+------------------------+----------------------------+------------------------------------------------+
| PYTHONPATH             | ``System Python Path``     | Path to the python executable, required with   |
|                        |                            | virtual environments                           |
+------------------------+----------------------------+------------------------------------------------+
| ENVIRONMENTTEXT        | ``None``                   | Text displayed on right of the logo. Useful    |
|                        |                            | to indicate different environments.            |
+------------------------+----------------------------+------------------------------------------------+
| ENVIRONMENTTEXTCOLOR   | Black                      | Color of the displayed PYTHONPATH. Use HTML    | 
|                        |                            | valid "color name" or #RGB values.             |
+------------------------+----------------------------+------------------------------------------------+
| LOGLEVEL               | INFO                       | Level for logging to log file. Values:         |
|                        |                            | DEBUG,INFO,STARTINFO,WARNING,ERROR or CRITICAL.| 
+------------------------+----------------------------+------------------------------------------------+
| LOGCONSOLE             | True                       | Console logging on (True) or off (False).      |
+------------------------+----------------------------+------------------------------------------------+
| LOGCONSOLELEVEL        | STARTINFO                  | level for logging to console/screen. Values:   | 
|                        |                            | DEBUG,INFO,STARTINFO,WARNING,ERROR or CRITICAL.| 
+------------------------+----------------------------+------------------------------------------------+
| MAXRETRIES             | 10                         | Maximum number of retries for failed outgoing  |
|                        |                            | messages                                       |
+------------------------+----------------------------+------------------------------------------------+
| MDNURL                 | ``None``                   | Return URL for receiving asynchronous MDNs from|
|                        |                            | partners.                                      |
+------------------------+----------------------------+------------------------------------------------+
| ASYNCMDNWAIT           | 30                         | Number of minutes to wait for asynchronous MDNs| 
|                        |                            | after which message will be marked as failed.  |
+------------------------+----------------------------+------------------------------------------------+
| MAXARCHDAYS            | 30                         | Number of days files and messages are kept in  |
|                        |                            | storage.                                       |
+------------------------+----------------------------+------------------------------------------------+
