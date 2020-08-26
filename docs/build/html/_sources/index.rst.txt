`QU4RTET AS2 Gateway's` Documentation!
======================================

`QU4RTET AS2 Gateway's` is a gateway the sends, receives, and forwards AS2 encrypted messages between Trading Partners and ``QU4RTET``.
The Gateway supports AS2 version 1.2 as defined in `RFC 4130`_.

The application includes a server for receiving files from partners, a front-end web interface for
configuration and monitoring, the ability to send messages, and asynchronous MDNs.

Features
--------

* Technical

    * Asynchronous and synchronous MDN
    * Partner and Organization management
    * Digital signatures
    * Message encryption
    * Secure transport (SSL)
    * Support for SSL client authentication
    * Data compression (AS2 1.1)

* Monitoring

    * Web interface for transaction monitoring
    * Email event notification

* The following encryption algorithms are supported:

    * Triple DES
    * DES
    * RC2-40
    * AES-128
    * AES-192
    * AES-256

* The following hash algorithms are supported:

    * SHA-1

Table of Contents:
------------------
.. toctree::
   :maxdepth: 2

   gettingstarted
   configuration
   changelog

.. _`RFC 4130`: https://www.ietf.org/rfc/rfc4130.txt
.. _`openssl`: https://wiki.openssl.org/index.php/Compilation_and_Installation
