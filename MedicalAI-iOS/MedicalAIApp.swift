import SwiftUI
import Foundation

// MARK: - Models
struct Medication: Identifiable {
    let id = UUID()
    let name: String
    let dosage: String
    let frequency: String
    let time: String
    let adherence: Double
}

struct Alert: Identifiable {
    let id = UUID()
    let type: String
    let message: String
    let icon: String
    let time: String
}

struct LabResult: Identifiable {
    let id = UUID()
    let testName: String
    let value: String
    let unit: String
    let reference: String
    let status: String
    let date: String
}

// MARK: - Main App
@main
struct MedicalAIApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

// MARK: - Content View
struct ContentView: View {
    @State private var selectedTab = 0
    
    var body: some View {
        TabView(selection: $selectedTab) {
            // Dashboard Tab
            DashboardView()
                .tabItem {
                    Label("דשבורד", systemImage: "house.fill")
                }
                .tag(0)
            
            // Medications Tab
            MedicationsView()
                .tabItem {
                    Label("תרופות", systemImage: "pills.fill")
                }
                .tag(1)
            
            // Alerts Tab
            AlertsView()
                .tabItem {
                    Label("התראות", systemImage: "bell.fill")
                }
                .tag(2)
            
            // Labs Tab
            LabResultsView()
                .tabItem {
                    Label("בדיקות", systemImage: "flask.fill")
                }
                .tag(3)
            
            // Profile Tab
            ProfileView()
                .tabItem {
                    Label("פרופיל", systemImage: "person.fill")
                }
                .tag(4)
        }
        .environment(\.layoutDirection, .rightToLeft)
    }
}

// MARK: - Dashboard View
struct DashboardView: View {
    var body: some View {
        NavigationView {
            ZStack {
                Color(UIColor(red: 0.95, green: 0.98, blue: 1.0, alpha: 1.0))
                    .ignoresSafeArea()
                
                ScrollView {
                    VStack(alignment: .trailing, spacing: 20) {
                        // Header
                        VStack(alignment: .trailing, spacing: 8) {
                            Text("🏥 מערכת בריאות דיגיטלית")
                                .font(.title2)
                                .fontWeight(.bold)
                            
                            Text("שלום, יוסי!")
                                .font(.headline)
                                .foregroundColor(.gray)
                        }
                        .frame(maxWidth: .infinity, alignment: .trailing)
                        .padding()
                        .background(Color.white)
                        .cornerRadius(12)
                        
                        // Health Status Cards
                        VStack(spacing: 12) {
                            HealthCard(
                                title: "דביקות תרופות",
                                value: "89%",
                                icon: "💊",
                                color: .green
                            )
                            
                            HealthCard(
                                title: "eGFR (כליות)",
                                value: "42",
                                icon: "🧬",
                                color: .red
                            )
                            
                            HealthCard(
                                title: "בדיקות קרובות",
                                value: "2",
                                icon: "📅",
                                color: .blue
                            )
                        }
                        
                        // Quick Actions
                        VStack(alignment: .trailing, spacing: 12) {
                            Text("פעולות מהירות")
                                .font(.headline)
                                .padding(.horizontal)
                            
                            HStack(spacing: 12) {
                                QuickActionButton(icon: "📸", label: "צילום בדיקה")
                                QuickActionButton(icon: "📧", label: "דוח שבועי")
                                QuickActionButton(icon: "🧪", label: "מחקרים")
                            }
                            .padding(.horizontal)
                        }
                        
                        // Recent Alerts
                        VStack(alignment: .trailing, spacing: 12) {
                            Text("התראות אחרונות")
                                .font(.headline)
                                .padding(.horizontal)
                            
                            RecentAlertItem(
                                icon: "⏰",
                                title: "זמן לקחת תרופה",
                                time: "עכשיו",
                                color: .blue
                            )
                            
                            RecentAlertItem(
                                icon: "🧪",
                                title: "בדיקת eGFR",
                                time: "בעוד שבועיים",
                                color: .orange
                            )
                        }
                        .padding(.horizontal)
                    }
                    .padding()
                }
            }
            .navigationTitle("דשבורד")
        }
    }
}

// MARK: - Medications View
struct MedicationsView: View {
    let medications = [
        Medication(name: "Dapagliflozin", dosage: "10mg", frequency: "פעם ביום", time: "09:00", adherence: 0.92),
        Medication(name: "Finerenone", dosage: "20mg", frequency: "פעם ביום", time: "09:00", adherence: 0.85),
        Medication(name: "Lisinopril", dosage: "10mg", frequency: "פעם ביום", time: "09:00", adherence: 0.88)
    ]
    
    var body: some View {
        NavigationView {
            ZStack {
                Color(UIColor(red: 0.95, green: 0.98, blue: 1.0, alpha: 1.0))
                    .ignoresSafeArea()
                
                VStack(alignment: .trailing, spacing: 0) {
                    List {
                        Section(header: Text("תרופות פעילות").font(.headline)) {
                            ForEach(medications) { med in
                                MedicationRow(medication: med)
                            }
                        }
                        
                        Section(header: Text("סטטיסטיקות").font(.headline)) {
                            VStack(alignment: .trailing, spacing: 12) {
                                StatRow(label: "דביקות ממוצעת", value: "88%", color: .green)
                                StatRow(label: "תרופות לקוחות היום", value: "3/3", color: .blue)
                                StatRow(label: "ימי דביקה", value: "45", color: .purple)
                            }
                            .padding()
                        }
                    }
                    .listStyle(.insetGrouped)
                }
            }
            .navigationTitle("תרופות")
            .navigationBarTitleDisplayMode(.inline)
        }
    }
}

// MARK: - Alerts View
struct AlertsView: View {
    let alerts = [
        Alert(type: "💊", message: "זמן לקחת Dapagliflozin 10mg", icon: "pill", time: "עכשיו"),
        Alert(type: "🧪", message: "בדיקת eGFR מתוכננת מחר", icon: "flask", time: "מחר 08:00"),
        Alert(type: "📢", message: "גילוי חדש: Tolvaptan טוב יותר ב-30%", icon: "megaphone", time: "היום")
    ]
    
    var body: some View {
        NavigationView {
            ZStack {
                Color(UIColor(red: 0.95, green: 0.98, blue: 1.0, alpha: 1.0))
                    .ignoresSafeArea()
                
                VStack {
                    List {
                        Section(header: Text("התראות פעילות").font(.headline)) {
                            ForEach(alerts) { alert in
                                HStack(spacing: 12) {
                                    Text(alert.type)
                                        .font(.title3)
                                    
                                    VStack(alignment: .leading, spacing: 4) {
                                        Text(alert.message)
                                            .font(.body)
                                            .fontWeight(.semibold)
                                        
                                        Text(alert.time)
                                            .font(.caption)
                                            .foregroundColor(.gray)
                                    }
                                    
                                    Spacer()
                                }
                                .padding(.vertical, 8)
                            }
                        }
                    }
                    .listStyle(.insetGrouped)
                }
            }
            .navigationTitle("התראות")
            .navigationBarTitleDisplayMode(.inline)
        }
    }
}

// MARK: - Lab Results View
struct LabResultsView: View {
    let results = [
        LabResult(testName: "Creatinine", value: "1.8", unit: "mg/dL", reference: "0.7-1.3", status: "high", date: "31/8/2026"),
        LabResult(testName: "eGFR", value: "42", unit: "mL/min", reference: ">60", status: "low", date: "31/8/2026"),
        LabResult(testName: "Potassium", value: "5.1", unit: "mmol/L", reference: "3.5-5.0", status: "high", date: "31/8/2026")
    ]
    
    var body: some View {
        NavigationView {
            ZStack {
                Color(UIColor(red: 0.95, green: 0.98, blue: 1.0, alpha: 1.0))
                    .ignoresSafeArea()
                
                VStack {
                    List {
                        Section(header: Text("בדיקות אחרונות").font(.headline)) {
                            ForEach(results) { result in
                                LabResultRow(result: result)
                            }
                        }
                    }
                    .listStyle(.insetGrouped)
                }
            }
            .navigationTitle("בדיקות דם")
            .navigationBarTitleDisplayMode(.inline)
        }
    }
}

// MARK: - Profile View
struct ProfileView: View {
    var body: some View {
        NavigationView {
            ZStack {
                Color(UIColor(red: 0.95, green: 0.98, blue: 1.0, alpha: 1.0))
                    .ignoresSafeArea()
                
                VStack {
                    List {
                        Section(header: Text("פרטים אישיים").font(.headline)) {
                            ProfileRow(label: "שם", value: "יוסי כהן")
                            ProfileRow(label: "גיל", value: "45")
                            ProfileRow(label: "מצב", value: "ADPKD")
                        }
                        
                        Section(header: Text("הגדרות").font(.headline)) {
                            NavigationLink(destination: Text("הודעות")) {
                                HStack(spacing: 12) {
                                    Text("🔔")
                                    Text("הודעות")
                                }
                            }
                            
                            NavigationLink(destination: Text("עזרה")) {
                                HStack(spacing: 12) {
                                    Text("❓")
                                    Text("עזרה")
                                }
                            }
                        }
                    }
                    .listStyle(.insetGrouped)
                }
            }
            .navigationTitle("פרופיל")
            .navigationBarTitleDisplayMode(.inline)
        }
    }
}

// MARK: - Supporting Views
struct HealthCard: View {
    let title: String
    let value: String
    let icon: String
    let color: Color
    
    var body: some View {
        HStack(spacing: 12) {
            VStack(alignment: .trailing, spacing: 4) {
                Text(title)
                    .font(.caption)
                    .foregroundColor(.gray)
                
                Text(value)
                    .font(.title3)
                    .fontWeight(.bold)
            }
            
            Spacer()
            
            Text(icon)
                .font(.title)
        }
        .padding()
        .background(Color.white)
        .cornerRadius(12)
        .shadow(radius: 2)
    }
}

struct QuickActionButton: View {
    let icon: String
    let label: String
    
    var body: some View {
        VStack(spacing: 8) {
            Text(icon)
                .font(.title2)
            
            Text(label)
                .font(.caption2)
                .lineLimit(2)
                .multilineTextAlignment(.center)
        }
        .frame(maxWidth: .infinity)
        .padding()
        .background(Color.white)
        .cornerRadius(12)
        .shadow(radius: 2)
    }
}

struct RecentAlertItem: View {
    let icon: String
    let title: String
    let time: String
    let color: Color
    
    var body: some View {
        HStack(spacing: 12) {
            Text(icon)
                .font(.title3)
            
            VStack(alignment: .leading, spacing: 2) {
                Text(title)
                    .font(.body)
                    .fontWeight(.semibold)
                
                Text(time)
                    .font(.caption)
                    .foregroundColor(.gray)
            }
            
            Spacer()
        }
        .padding()
        .background(Color.white)
        .cornerRadius(12)
    }
}

struct MedicationRow: View {
    let medication: Medication
    
    var body: some View {
        VStack(alignment: .trailing, spacing: 8) {
            HStack(spacing: 12) {
                Text("💊")
                
                VStack(alignment: .leading, spacing: 2) {
                    Text(medication.name)
                        .font(.body)
                        .fontWeight(.semibold)
                    
                    Text("\(medication.dosage) • \(medication.frequency)")
                        .font(.caption)
                        .foregroundColor(.gray)
                }
                
                Spacer()
            }
            
            // Adherence Bar
            VStack(alignment: .trailing, spacing: 4) {
                HStack {
                    Text("דביקות: \(Int(medication.adherence * 100))%")
                        .font(.caption)
                        .foregroundColor(.gray)
                    
                    Spacer()
                }
                
                ProgressView(value: medication.adherence)
                    .tint(.green)
            }
        }
        .padding(.vertical, 8)
    }
}

struct LabResultRow: View {
    let result: LabResult
    
    var body: some View {
        HStack(spacing: 12) {
            VStack(alignment: .trailing, spacing: 4) {
                Text(result.testName)
                    .font(.body)
                    .fontWeight(.semibold)
                
                HStack(spacing: 4) {
                    Text(result.reference)
                        .font(.caption)
                        .foregroundColor(.gray)
                    
                    Text("•")
                        .foregroundColor(.gray)
                    
                    Text(result.date)
                        .font(.caption)
                        .foregroundColor(.gray)
                }
            }
            
            Spacer()
            
            VStack(alignment: .trailing, spacing: 2) {
                Text("\(result.value) \(result.unit)")
                    .font(.body)
                    .fontWeight(.bold)
                
                Text(result.status == "high" ? "⬆️ גבוה" : "⬇️ נמוך")
                    .font(.caption)
                    .foregroundColor(result.status == "high" ? .red : .blue)
            }
        }
        .padding(.vertical, 8)
    }
}

struct StatRow: View {
    let label: String
    let value: String
    let color: Color
    
    var body: some View {
        HStack {
            Text(label)
                .font(.body)
            
            Spacer()
            
            Text(value)
                .font(.body)
                .fontWeight(.bold)
                .foregroundColor(color)
        }
    }
}

struct ProfileRow: View {
    let label: String
    let value: String
    
    var body: some View {
        HStack {
            Text(label)
                .foregroundColor(.gray)
            
            Spacer()
            
            Text(value)
                .fontWeight(.semibold)
        }
    }
}

#Preview {
    ContentView()
}
