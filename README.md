
<h1 align="center">Welcome to SQL-builder 💻</h1>  
  
<div align="center">  
    <img src="logo.gif" alt="The logo" width=500">  
</div>   


<div align="center">
  <img src="https://forthebadge.com/images/badges/you-didnt-ask-for-this.svg" />
</div>

<div align="center">
    <img src="https://forthebadge.com/images/badges/built-with-love.svg" />

  <a href="https://python.org/">
    <img src="https://forthebadge.com/images/badges/made-with-python.svg" />
  </a>
</div>
    

## Description 📝  
  
I was studying the builder pattern and decided to apply in a "real problem".  
This was a funny project to do, but please: **Don't take it seriously**
> This project does not want in any way be a product, the-best-solution nor compete with any other similar project, this is just a the result of a learning process :rocket:  
> > If you are searching for a real SQL builder using python, please check out at [PyPika](https://github.com/kayak/pypika) or [Ibis](https://ibis-project.org/) 

## How to use :pencil2:  
```shell
>>> from builder import Select

# Note that you can call explicitly .sql() or let __repr__ eval as str.
>>> Select('field').from_('table')
SELECT field FROM table;

>>> Select('field').from_('table').where_('field = 1')
SELECT field FROM table WHERE field = 1;

>>> Select('field0, field1').from_('table').where_('field0 = 0').or_('field1 = 1')
SELECT field0, field1 FROM table WHERE field0 = 0 OR field1 = 1;

>>> Select('field').from_('table').group_by_("field").order_by_("field")
SELECT field FROM table GROUP BY field ORDER BY field;

>>> Select().from_('table').limit_(10)
SELECT * FROM table LIMIT 10;
```

> You can also verify all examples and test then at `python examples.py`.

## Author  
  
👤 **Vinicius Kammradt**  
  
* Website: https://kammradt.now.sh/  
* Twitter: [@kammzinho](https://twitter.com/kammzinho)  
* Github: [@kammradt](https://github.com/kammradt)  
* LinkedIn: [@vinicius-kammradt](https://linkedin.com/in/vinicius-kammradt)
