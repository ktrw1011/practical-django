from django.db import models

class DraftSnippetManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_draft=True)

class SnippetQuerySet(models.QuerySet):
    def drafts(self):
        return self.filter(is_draft=True)

    def recent_updates(self):
        return self.order_by("-updated_at")

    # queryset_only=TrueにするとSnippets.objectsから呼べなくなる
    # recent_updatesはQuerySetから呼ぶものなので属性をつけたほうがいい
    recent_updates.queryset_only = True

class Snippet(models.Model):
    title = models.CharField('タイトル', max_length=128)
    description = models.TextField('説明', blank=True)
    is_draft = models.BooleanField('Draft', default=True)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    # 自身でManagerを定義している場合
    # models.Managerを差し込むために必ず指定
    # objects = models.Manager()
    # Snippets.drafts.all()の用に使用可能
    # drafts = DraftSnippetManager()
    
    # 独自のQuerySetをカスタマイズしてそれSnippets.objectsとして扱える
    # objects = SnippetQuerySet.as_manager()

    # QuerySetとManagerどちらもカスタマイズした場合は以下の様にかける
    # objects = DraftSnippetManager.from_queryset(SnippetQuerySet)()

    def __str__(self) -> str:
        return f'{self.pk} {self.title}'


class Comment(models.Model):
    text = models.TextField("本文", blank=False)
    commented_to = models.ForeignKey(Snippet, verbose_name="スニペット", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.pk} {self.text}"

class Tag(models.Model):
    name = models.CharField("タグ名", max_length=32)
    snippets = models.ManyToManyField(Snippet, related_name="tags", related_query_name="tag")

    def __str__(self) -> str:
        return f"{self.pk} {self.name}"