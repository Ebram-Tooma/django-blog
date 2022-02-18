from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# def home (request):
#     return render(request, 'home.html',{})

#like view
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
        
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

# home posts list view
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    # ordering = ['-post_date']
    
    #categories menu
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    
#creating category list view  
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})
    
#creating category view for listing all posts in this category with replacing any space with - in url 
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats, 'category_posts':category_posts})
    # category_posts = Post.objects.filter(category=cats.replace('-',' '))
    # return render(request, 'categories.html', {'cats':cats.title().replace('-',' '), 'category_posts':category_posts})




#post details view
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    #categories menu and likes
    def get_context_data(self, *args, **kwargs):
        #category menu variable
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        
        #like variable 
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        #liked condition
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
            
        #passing variables to context
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked

        return context
    

#adding post view
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields = '__all__'
    # fields = ('title', 'title_tag', 'author', 'body', )


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    # fields = '__all__'
    # fields = ('title', 'title_tag', 'author', 'body', )
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.post_id =self.kwargs['pk']
        return super().form_valid(form)
        

    
# adding category view
class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = "add_category.html"
    fields = '__all__'
    # fields = ('title', 'title_tag', 'author', 'body', )

# editing post view
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ('title', 'title_tag', 'body', )

# delete post view

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')
