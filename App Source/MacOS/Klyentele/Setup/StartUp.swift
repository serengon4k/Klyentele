//
//  ContentView.swift
//  Klyentele
//
//  Created by Devin B on 4/6/22.
//

import SwiftUI
enum Step {
    case start
    case legal
    case modeSelection
    case licensekey
}

struct StartUp: View {
    
    @State private var StartStep: Step =  .licensekey
    var body: some View {
            switch StartStep {
                case .start: Starting(CurrentTab: $StartStep).transition(.asymmetric(insertion: .move(edge: .leading), removal: .move(edge: .leading)))
                    
                case .legal: Legal(CurrentTab: $StartStep).transition(.asymmetric(insertion: .move(edge: .leading), removal: .move(edge: .leading)))
                    
                    
                case .modeSelection: ModeSelection(CurrentTab: $StartStep).transition(.asymmetric(insertion: .move(edge: .leading), removal: .move(edge: .leading)))
                    
                case .licensekey: LicenseKey(CurrentTab: $StartStep).transition(.asymmetric(insertion: .move(edge: .leading), removal: .move(edge: .leading)))
            }
        
    }
    
}


struct Starting: View {
    @Binding var CurrentTab: Step
    var body: some View {
        VStack(alignment: .center)
        {
            //Logo
            Image("Logo")
                .resizable(resizingMode: .stretch)
                .aspectRatio(contentMode: .fill)
                .frame(width: 200, height: 200)
            //Text
            VStack(alignment: .leading) {
                //Klyentele
                Text("Klyentele").font(.custom("Montserrat", size: 48)).foregroundColor(.primary)
                //by Azura4k
                Text("by Azura4k").font(.custom("Montserrat", size: 14)).foregroundColor(.primary)
            }
            Spacer().frame(height: 30)
            
            
            Button("Next"){
                CurrentTab = .legal
            }.buttonStyle(NormalButton())
            
            
            
            Button("About"){}.buttonStyle(NormalButton())
        }.frame(width:884,height: 647).background(.background)
    }
}

struct Legal: View {
    @Binding var CurrentTab: Step
    var body: some View {
        VStack(alignment: .leading)
        {
            HStack (alignment: .top) {
                Image("Logo")
                    .resizable(resizingMode: .stretch)
                    .aspectRatio(contentMode: .fill)
                    .frame(width: 60, height: 60)
                Text("The Legal Stuff").font(.custom("Montserrat", size: 48)).foregroundColor(.primary)
            }
            Spacer().frame(height: 50)
            HStack () {
                Text("Before we can continue, please read the following documents listed below:").font(.custom("Montserrat", size: 24)).foregroundColor(.primary)
               
            }

            HStack () {
                Text("Once done, click the corossponding choice.").font(.custom("Montserrat", size: 24)).foregroundColor(.primary)
               
            }
            Spacer().frame(height: 50)
            
            HStack () {
                Button("I Agree"){
                    CurrentTab = .modeSelection
                }.buttonStyle(NormalButton())
                Spacer().frame(width: 50)
                Button("I Disagree"){
                    CurrentTab = .start
                }.buttonStyle(NormalButton())
            }
           
            
         
        }.frame(width:884,height: 647).background(.background)
    }
}

struct ModeSelection: View {
    @Binding var CurrentTab: Step
    var body: some View {
        VStack(alignment: .center)
        {
            //Text
            VStack(alignment: .center) {
                //Title
                VStack {
                Text("Welcome").font(.custom("Montserrat", size: 48)).foregroundColor(.primary)
                Text("Please Select Your Mode").font(.custom("Montserrat", size: 32)).foregroundColor(.primary)
                }
                // Buttons
                HStack {
                    VStack{
                    Button("\(Image(systemName: "person"))"){
                        
                        CurrentTab = .modeSelection
                    }.buttonStyle(ModeSelectionButton())
                        Text("Solo").font(.custom("Montserrat", size: 32)).foregroundColor(.primary)
                    }
                    Spacer().frame(width: 100)
                    VStack{
                    Button("\(Image(systemName: "person.3"))"){
                        
                        CurrentTab = .modeSelection
                    }.buttonStyle(ModeSelectionButton())
                        Text("Team").font(.custom("Montserrat", size: 32)).foregroundColor(.primary)
                    }
                }
                
                
                
            }
            Spacer().frame(height: 30)
            
            Button("Next"){
                CurrentTab = .licensekey
            }.buttonStyle(NormalButton())
            
        }.frame(width:884,height: 647).background(.background)
    }
}

struct LicenseKey: View {
    @Binding var CurrentTab: Step
    @State var LicenseKey = ""
    @State var DeviceID = ""
    
    var body: some View {
        VStack(alignment: .center)
        {
            VStack(alignment: .center) {
                //Title
                VStack {
                Text("Great").font(.custom("Montserrat", size: 48)).foregroundColor(.primary)
                Text("Please Enter your License Key").font(.custom("Montserrat", size: 32)).foregroundColor(.primary)
                    
                TextField("License Key", text: LicenseKey)
                }
            //Text
            VStack(alignment: .leading) {
                //Klyentele
                Text("Klyentele").font(.custom("Montserrat", size: 48)).foregroundColor(.primary)
                //by Azura4k
                Text("by Azura4k").font(.custom("Montserrat", size: 14)).foregroundColor(.primary)
            }
            Spacer().frame(height: 30)
            
        
        }.frame(width:884,height: 647).background(.background)
    }
}



struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        StartUp().preferredColorScheme(.dark)
    }
}
}
