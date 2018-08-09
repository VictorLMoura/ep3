import 'package:flutter/material.dart';

//import '../models/modelo_bar.dart';
import '../pages/bar_detalhe.dart';
import '../scope_models/main_model.dart';

class BarCard extends StatelessWidget {
  final MainModel model;
  final int index;
  BarCard(this.model, this.index);

  @override
  Widget build(BuildContext context) {
    final bar = model.bares[index];
    return GestureDetector(
      onTap: () {
        Navigator.of(context).push(
          MaterialPageRoute(builder: (BuildContext context) {
            return PaginaBarDetalhe(index, model);
          }),
        );
      },
      child: Container(
          height: 180.0,
          decoration: BoxDecoration(
            image: DecorationImage(
              image: AssetImage(bar.image),
              fit: BoxFit.cover,
              /*  colorFilter: ColorFilter.mode(
                Colors.black.withOpacity(0.3), BlendMode.dstATop), */
            ),
          ),
          child: Column(
            children: <Widget>[
              SizedBox(
                height: 132.0,
              ),
              Container(
                height: 48.0,
                decoration: BoxDecoration(
                    /*  borderRadius: BorderRadius.circular(10.0), */ 
                    color: Colors.black.withOpacity(0.6)),
                child: Column(
                  children: <Widget>[
                    Container(
                      alignment: AlignmentDirectional(-0.95, 1.0),
                      child: Text(bar.name,
                          style: TextStyle(
                              color: Theme.of(context).accentColor,
                              fontSize: 16.0),
                          textAlign: TextAlign.right),
                      /*  decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(10.0),
                              color: Colors.black.withOpacity(0.7)), */
                    ),
                    Container(
                      margin:
                          EdgeInsets.only( bottom: 3.0),
                      /* decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(10.0),
                          color: Colors.black.withOpacity(0.5)), */
                      padding: EdgeInsets.symmetric(horizontal: 10.0),
                      child: Row(
                        children: <Widget>[
                          Text(
                            bar.address,
                            style:
                                TextStyle(color: Colors.grey, fontSize: 13.0),
                          ),
                          Text(
                            bar.distance,
                            style:
                                TextStyle(color: Colors.grey, fontSize: 13.0),
                          ),
                        ],
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      ),
                    ),
                  ],
                ),
              )
            ],
          )),
    );
  }
}
