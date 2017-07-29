user action
===============

- AddUser(UserDTO)
- UpdateUser(UserDTO, my_user or admin_user)
- RemoveUser(UserDTO, my_user or admin_user)
- EscalationAdmin(UserDTO, admin_user)

user query
============
- GetUser(user_id)
- GetUsers()

tenant action
================

- CreateTenant(TenantDTO, admin_user)
- UpdateTenant(TenantDTO, maintainer_user or admin_user)
- DisableTenant(TenantDTO, admin_user)
- EnableTenant(TenantDTO, admin_user)
- RemoveTenant(TenantDTO, admin_user)

tenant query
===============

- GetTenant(tenant_id)
- GetTenants()

maintainer action
=====================

- AddMaintanierTenant(UserDTO, TenantDTO, maintainer_user or admin_user)
- RemoveMaintainerTenant(UserDTO, TenantDTO, maintainer_user or admin_user)

maintainer query
======================

- GetMaintainer(maintainer_id)
- GetMaintainersByTenantId(tenant_id)

author action
======================

- CreateAuthor(AuthorDTO, TenantDTO, user)
- UpdateAuthor(AuthorDTO, author_user or admin_user or maintainer_user)
- RemoveAuthor(AuthorDTO, author_user or admin_user or maintainer_user)

author query
==================

- GetAuthor(author_id)
- GetAuthorsByTenantId(tenant_id)
- GetAuthorsByUserId(user_id)

author belong action
=========================

- BelongUserToAuthor(UserDTO, AuthorDTO, author_user or admin_user or maintainer_user)
- SecedeUserFromAuthor(UserDTO, AuthorDTO, author_user or admin_user or maintainer_user)

articles action
====================

- CreateArticle(ArticleDTO, author)
- RemoveArticle(ArticleDTO, author)
- UpdateArticle(ArticleDTO, author)

articles query
====================

- GetArticlesByTenantId(tenant_id)
- GetArticlesByAuthorId(author_id
- GetTags()
- GetTag(tag_id)

comment action
=================

- CreateCommentByGuest(CommentDTO, ArticleDTO)
- CreateCommentByAuthor(CommentDTO, author)
- RemoveComment(CommentDTO, article_author or admin_user or maintainer_user)

comment query
=================

- GetCommentsByTenantId(tenant_id)
- GetCommentsByArticleId(article_id)
- GetCommentsByAuthorId(author_id)
